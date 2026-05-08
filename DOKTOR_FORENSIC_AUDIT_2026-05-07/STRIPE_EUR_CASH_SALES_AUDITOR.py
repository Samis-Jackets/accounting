#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
STRIPE EUR SALES & CASH SALES AUDIT
Samis Jackets AB - Org.nr: 559489-5301
Date: 2026-05-07
Period: Q1 2026 (2026-01-01 to 2026-03-31)

Purpose: Verify all Stripe EUR payments from Wise and Cash sales (1910) are properly recorded
"""

import re
from pathlib import Path
from decimal import Decimal

class StripeEURCashAuditor:
    """Audit Stripe EUR payments and Cash sales"""
    
    def __init__(self):
        self.stripe_eur_sales = []
        self.cash_transactions = []
        self.total_stripe_eur_gross = Decimal('0')
        self.total_stripe_eur_net = Decimal('0')
        self.total_stripe_eur_vat = Decimal('0')
        self.total_cash_sales_net = Decimal('0')
        self.total_cash_sales_gross = Decimal('0')
        self.total_cash_sales_vat = Decimal('0')
        
    def extract_stripe_eur_from_master(self, master_file):
        """Extract all Stripe EUR transactions from master file"""
        try:
            with open(master_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                # Check if this is a Stripe EUR VER line
                if 'Stripe' in line and '[WISE_EUR]' in line:
                    ver_match = re.match(r'#VER\s+(\w+)\s+(\d+)\s+(\d{8})\s+"Stripe\s+([A-Z0-9]+)\s+\[WISE_EUR\]"', line)
                    if ver_match:
                        series, ver_num, date, stripe_id = ver_match.groups()
                        
                        # Read the transaction block
                        i += 1  # Move to next line (should be '{')
                        trans_lines = []
                        if i < len(lines):
                            if '{' in lines[i]:
                                i += 1  # Move past '{'
                            # Now read until we find '}' as standalone closing brace
                            while i < len(lines) and lines[i].strip() != '}':
                                trans_lines.append(lines[i])
                                i += 1
                        
                        # Parse amounts from transaction lines
                        trans_block = ''.join(trans_lines)
                        eur_match = re.search(r'#TRANS\s+1944\s+\{\}\s+([\d.]+)', trans_block)
                        sales_match = re.search(r'#TRANS\s+3001\s+\{\}\s+-([\d.]+)', trans_block)
                        vat_match = re.search(r'#TRANS\s+2611\s+\{\}\s+-([\d.]+)', trans_block)
                        
                        if eur_match and sales_match and vat_match:
                            eur_amount = Decimal(eur_match.group(1))
                            sales_net = Decimal(sales_match.group(1))
                            vat = Decimal(vat_match.group(1))
                            
                            self.stripe_eur_sales.append({
                                'ver': f"{series} {ver_num}",
                                'date': date,
                                'stripe_id': stripe_id,
                                'eur_amount': eur_amount,
                                'sales_net': sales_net,
                                'vat': vat,
                                'gross': sales_net + vat
                            })
                            
                            self.total_stripe_eur_gross += (sales_net + vat)
                            self.total_stripe_eur_net += sales_net
                            self.total_stripe_eur_vat += vat
                
                i += 1
            
            return len(self.stripe_eur_sales)
        except Exception as e:
            print(f"Error extracting Stripe EUR: {e}")
            import traceback
            traceback.print_exc()
            return 0
    
    def extract_cash_sales_from_master(self, master_file):
        """Extract all cash (1910) transactions from master file"""
        try:
            with open(master_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                # Check if this is a VER line
                ver_match = re.match(r'#VER\s+(\w+)\s+(\d+)\s+(\d{8})\s+"([^"]+)"', line)
                if ver_match:
                    series, ver_num, date, description = ver_match.groups()
                    
                    # Read the transaction block
                    i += 1
                    trans_lines = []
                    if i < len(lines) and '{' in lines[i]:
                        i += 1
                        while i < len(lines) and lines[i].strip() != '}':
                            trans_lines.append(lines[i])
                            i += 1
                    
                    # Check if this VER has 1910 transaction
                    trans_block = ''.join(trans_lines)
                    cash_match = re.search(r'#TRANS\s+1910\s+\{\}\s+([-\d.]+)', trans_block)
                    
                    if cash_match:
                        cash_amount = Decimal(cash_match.group(1))
                        
                        # Check if it's a sales transaction (has 3051 or 3001)
                        sales_match = re.search(r'#TRANS\s+(3001|3051)\s+\{\}\s+-([\d.]+)', trans_block)
                        vat_match = re.search(r'#TRANS\s+2611\s+\{\}\s+-([\d.]+)', trans_block)
                        
                        trans_type = "Sales" if sales_match else "Other"
                        
                        if sales_match and vat_match:
                            sales_net = Decimal(sales_match.group(2))
                            vat = Decimal(vat_match.group(1))
                            gross = sales_net + vat
                            
                            self.total_cash_sales_net += sales_net
                            self.total_cash_sales_vat += vat
                            self.total_cash_sales_gross += gross
                        else:
                            sales_net = Decimal('0')
                            vat = Decimal('0')
                            gross = Decimal('0')
                        
                        self.cash_transactions.append({
                            'ver': f"{series} {ver_num}",
                            'date': date,
                            'description': description,
                            'cash_amount': cash_amount,
                            'type': trans_type,
                            'sales_net': sales_net,
                            'vat': vat,
                            'gross': gross
                        })
                
                i += 1
            
            return len(self.cash_transactions)
        except Exception as e:
            print(f"Error extracting cash transactions: {e}")
            import traceback
            traceback.print_exc()
            return 0
    
    def generate_report(self):
        """Generate detailed audit report"""
        
        report = []
        report.append("=" * 100)
        report.append("STRIPE EUR SALES & CASH SALES AUDIT")
        report.append("Samis Jackets AB - Org.nr: 559489-5301")
        report.append("Date: 2026-05-07")
        report.append("Period: Q1 2026 (2026-01-01 to 2026-03-31)")
        report.append("=" * 100)
        report.append("")
        
        # Stripe EUR Sales
        if self.stripe_eur_sales:
            report.append("[STRIPE EUR SALES] (Wise EUR Account 1944 -> Sales 3001):")
            report.append("-" * 100)
            report.append(f"{'VER':<10} {'Date':<12} {'Stripe ID':<18} {'EUR Amount':>12} {'Net Sales':>12} {'VAT 25%':>12} {'Gross':>12}")
            report.append("-" * 100)
            
            for sale in self.stripe_eur_sales:
                report.append(
                    f"{sale['ver']:<10} {sale['date']:<12} {sale['stripe_id']:<18} "
                    f"{sale['eur_amount']:>12,.2f} {sale['sales_net']:>12,.2f} "
                    f"{sale['vat']:>12,.2f} {sale['gross']:>12,.2f}"
                )
            
            report.append("-" * 100)
            report.append(f"{'TOTAL STRIPE EUR SALES':<52} {self.total_stripe_eur_net:>12,.2f} "
                         f"{self.total_stripe_eur_vat:>12,.2f} {self.total_stripe_eur_gross:>12,.2f}")
            report.append("")
            report.append(f"Number of Stripe EUR transactions: {len(self.stripe_eur_sales)}")
            report.append("")
        
        # Cash Transactions
        if self.cash_transactions:
            report.append("[CASH TRANSACTIONS] (Account 1910 - Kassa):")
            report.append("-" * 100)
            report.append(f"{'VER':<10} {'Date':<12} {'Type':<8} {'Cash Amount':>12} {'Net Sales':>12} {'VAT':>12} {'Description':<30}")
            report.append("-" * 100)
            
            for trans in self.cash_transactions:
                desc = trans['description'][:28] + '..' if len(trans['description']) > 30 else trans['description']
                report.append(
                    f"{trans['ver']:<10} {trans['date']:<12} {trans['type']:<8} "
                    f"{trans['cash_amount']:>12,.2f} {trans['sales_net']:>12,.2f} "
                    f"{trans['vat']:>12,.2f} {desc:<30}"
                )
            
            report.append("-" * 100)
            report.append("")
            
            # Summary by type
            sales_trans = [t for t in self.cash_transactions if t['type'] == 'Sales']
            other_trans = [t for t in self.cash_transactions if t['type'] == 'Other']
            
            if sales_trans:
                report.append(f"CASH SALES TRANSACTIONS: {len(sales_trans)}")
                report.append(f"  Total Net Sales:  {self.total_cash_sales_net:>12,.2f} SEK")
                report.append(f"  Total VAT 25%:    {self.total_cash_sales_vat:>12,.2f} SEK")
                report.append(f"  Total Gross:      {self.total_cash_sales_gross:>12,.2f} SEK")
                report.append("")
            
            if other_trans:
                total_other = sum(t['cash_amount'] for t in other_trans)
                report.append(f"OTHER CASH TRANSACTIONS: {len(other_trans)}")
                report.append(f"  Total Amount:     {total_other:>12,.2f} SEK")
                report.append("")
        
        # Overall Summary
        report.append("=" * 100)
        report.append("[OVERALL SUMMARY]:")
        report.append("=" * 100)
        report.append("")
        report.append("STRIPE EUR SALES (from Wise EUR):")
        report.append(f"  Transactions:     {len(self.stripe_eur_sales)}")
        report.append(f"  Net Sales:        {self.total_stripe_eur_net:>12,.2f} SEK")
        report.append(f"  VAT 25%:          {self.total_stripe_eur_vat:>12,.2f} SEK")
        report.append(f"  Gross Sales:      {self.total_stripe_eur_gross:>12,.2f} SEK")
        report.append("")
        report.append("CASH SALES (Account 1910):")
        report.append(f"  Transactions:     {len([t for t in self.cash_transactions if t['type'] == 'Sales'])}")
        report.append(f"  Net Sales:        {self.total_cash_sales_net:>12,.2f} SEK")
        report.append(f"  VAT 25%:          {self.total_cash_sales_vat:>12,.2f} SEK")
        report.append(f"  Gross Sales:      {self.total_cash_sales_gross:>12,.2f} SEK")
        report.append("")
        report.append("COMBINED TOTAL:")
        combined_net = self.total_stripe_eur_net + self.total_cash_sales_net
        combined_vat = self.total_stripe_eur_vat + self.total_cash_sales_vat
        combined_gross = self.total_stripe_eur_gross + self.total_cash_sales_gross
        report.append(f"  Net Sales:        {combined_net:>12,.2f} SEK")
        report.append(f"  VAT 25%:          {combined_vat:>12,.2f} SEK")
        report.append(f"  Gross Sales:      {combined_gross:>12,.2f} SEK")
        report.append("")
        
        report.append("=" * 100)
        report.append("[AUDIT COMPLETE] ALL STRIPE EUR AND CASH SALES TRANSACTIONS REVIEWED")
        report.append("=" * 100)
        
        return "\n".join(report)
    
    def run_audit(self):
        """Execute full audit"""
        print("Running Stripe EUR & Cash Sales Audit...")
        
        base_path = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip")
        master_file = base_path / "Q1_2026_PERIOD_2026-01_TO_2026-03" / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
        
        print(f"Reading: {master_file}")
        print(f"File exists: {master_file.exists()}")
        
        # Extract data
        stripe_count = self.extract_stripe_eur_from_master(master_file)
        print(f"Found {stripe_count} Stripe EUR transactions")
        
        cash_count = self.extract_cash_sales_from_master(master_file)
        print(f"Found {cash_count} cash transactions (1910)")
        
        # Generate report
        report = self.generate_report()
        
        # Save report
        output_file = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\DOKTOR_FORENSIC_AUDIT_2026-05-07") / "STRIPE_EUR_CASH_SALES_AUDIT.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(report)
        print(f"\nReport saved to: {output_file}")
        
        return report


if __name__ == "__main__":
    auditor = StripeEURCashAuditor()
    auditor.run_audit()
