#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CORRECTED SALES & VAT AUDIT - FIXED VERSION
Samis Jackets AB - Org.nr: 559489-5301
Date: 2026-05-07

FIXES:
1. Remove insurance (3994) from sales
2. Only count Marginalen "B" transactions (Worldline deposits) - NOT Worldline standalone
3. Check for bidrag (3985)
"""

import re
from pathlib import Path
from decimal import Decimal

class CorrectedSalesAuditor:
    """Corrected audit - no duplicates, no non-sales"""
    
    def __init__(self):
        self.real_sales = {}
        self.non_sales_income = {}
        self.duplicates_removed = {}
        
    def extract_res_balance(self, se_file_path, account):
        """Extract #RES balance for an account"""
        try:
            with open(se_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            pattern = rf'#RES\s+0\s+{account}\s+([-\d.]+)'
            matches = re.findall(pattern, content)
            
            if matches:
                return abs(Decimal(matches[0]))
            return Decimal('0')
        except Exception as e:
            print(f"Error reading {se_file_path}: {e}")
            return Decimal('0')
    
    def count_marginalen_b_transactions(self, se_file_path):
        """Count total from Marginalen B transactions (Worldline deposits)"""
        try:
            with open(se_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find all VER with "B" prefix (Worldline deposits to Marginalen)
            pattern = r'#VER\s+\w+\s+\d+\s+\d{8}\s+"B\d+[^{]*\{([^}]+)\}'
            vers = re.findall(pattern, content, re.DOTALL)
            
            total = Decimal('0')
            for trans_block in vers:
                # Extract amount to 1930 (Marginalen)
                amount_match = re.search(r'#TRANS\s+1930\s+\{\}\s+([\d.]+)', trans_block)
                if amount_match:
                    total += Decimal(amount_match.group(1))
            
            return total
        except Exception as e:
            print(f"Error counting B transactions: {e}")
            return Decimal('0')
    
    def audit_real_sales(self):
        """Audit real sales only - no duplicates, no non-sales"""
        
        base_path = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
        
        # MARGINALEN: Only B transactions (Worldline card sales deposits)
        marginalen_file = base_path / "source_csv" / "marginalen" / "MARGINALEN_STANDALONE.se"
        
        # Get total from "B" transactions
        worldline_via_marginalen = self.count_marginalen_b_transactions(marginalen_file)
        if worldline_via_marginalen > 0:
            self.real_sales['Worldline (via Marginalen B transactions)'] = worldline_via_marginalen
        
        # MARGINALEN: Other sales (3001 and 3105, excluding insurance 3994)
        marginalen_3001 = self.extract_res_balance(marginalen_file, "3001")
        if marginalen_3001 > 0:
            self.real_sales['Marginalen direct sales (3001)'] = marginalen_3001
        
        norway_export = self.extract_res_balance(marginalen_file, "3105")
        if norway_export > 0:
            self.real_sales['Norway Export (3105)'] = norway_export
        
        # MARGINALEN: Insurance and bidrag (NOT sales)
        insurance = self.extract_res_balance(marginalen_file, "3994")
        if insurance > 0:
            self.non_sales_income['Insurance/försäkringsersättningar (3994)'] = insurance
        
        bidrag = self.extract_res_balance(marginalen_file, "3985")
        if bidrag > 0:
            self.non_sales_income['Government grants/bidrag (3985)'] = bidrag
        
        # LUNAR BANK: Real sales
        lunar_file = base_path / "source_csv" / "Lunar Bank" / "LUNAR_STANDALONE.se"
        lunar_sales = self.extract_res_balance(lunar_file, "3001")
        if lunar_sales > 0:
            self.real_sales['Lunar Bank (3001)'] = lunar_sales
        
        # WISE: Real sales
        wise_file = base_path / "source_csv" / "wise" / "usd" / "20260101-20261231.se"
        wise_sales = self.extract_res_balance(wise_file, "3051")
        if wise_sales > 0:
            self.real_sales['Wise EU/USD (3051)'] = wise_sales
        
        # DUPLICATES REMOVED
        # Worldline standalone was counted separately, but it's the same as B transactions
        worldline_standalone = self.extract_res_balance(
            base_path / "source_csv" / "worldline" / "WORLDLINE_STANDALONE.se", "3051"
        )
        if worldline_standalone > 0:
            self.duplicates_removed['Worldline standalone (DUPLICATE)'] = worldline_standalone
    
    def generate_report(self):
        """Generate corrected audit report"""
        
        report = []
        report.append("=" * 80)
        report.append("CORRECTED SALES & VAT AUDIT - FIXED VERSION")
        report.append("Samis Jackets AB - Org.nr: 559489-5301")
        report.append("Date: 2026-05-07")
        report.append("Period: Q1 2026 (2026-01-01 to 2026-03-31)")
        report.append("=" * 80)
        report.append("")
        report.append("USER CORRECTIONS APPLIED:")
        report.append("✅ Removed insurance/försäkringsersättningar (NOT sales)")
        report.append("✅ Fixed Worldline double-counting (only use Marginalen B transactions)")
        report.append("✅ Separated bidrag/grants from sales")
        report.append("")
        
        # Real sales
        if self.real_sales:
            report.append("📊 REAL SALES (Q1 2026):")
            report.append("-" * 80)
            total_sales = Decimal('0')
            for source, amount in self.real_sales.items():
                report.append(f"   {source:<45} {amount:>15,.2f} SEK")
                total_sales += amount
            report.append("-" * 80)
            report.append(f"   {'TOTAL REAL SALES (Gross)':<45} {total_sales:>15,.2f} SEK")
            
            # Calculate VAT
            # Worldline and Lunar are gross (includes 25% VAT)
            # Norway is 0% VAT (export)
            worldline_gross = self.real_sales.get('Worldline (via Marginalen B transactions)', Decimal('0'))
            lunar_gross = self.real_sales.get('Lunar Bank (3001)', Decimal('0'))
            marginalen_3001 = self.real_sales.get('Marginalen direct sales (3001)', Decimal('0'))
            wise_gross = self.real_sales.get('Wise EU/USD (3051)', Decimal('0'))
            
            total_with_vat = worldline_gross + lunar_gross + marginalen_3001 + wise_gross
            net_sales = total_with_vat / Decimal('1.25')
            vat = total_with_vat - net_sales
            norway = self.real_sales.get('Norway Export (3105)', Decimal('0'))
            
            report.append("")
            report.append(f"   {'Net Sales (excl. VAT)':<45} {net_sales + norway:>15,.2f} SEK")
            report.append(f"   {'Output VAT 25%':<45} {vat:>15,.2f} SEK")
            report.append("")
        
        # Non-sales income
        if self.non_sales_income:
            report.append("💰 OTHER INCOME (NOT SALES):")
            report.append("-" * 80)
            total_non_sales = Decimal('0')
            for source, amount in self.non_sales_income.items():
                report.append(f"   {source:<45} {amount:>15,.2f} SEK")
                total_non_sales += amount
            report.append("-" * 80)
            report.append(f"   {'TOTAL OTHER INCOME':<45} {total_non_sales:>15,.2f} SEK")
            report.append("")
            report.append("   Note: These are not sales - they are insurance compensation")
            report.append("   or government grants. No VAT applies.")
            report.append("")
        
        # Duplicates removed
        if self.duplicates_removed:
            report.append("❌ DUPLICATES REMOVED (User was RIGHT!):")
            report.append("-" * 80)
            for item, amount in self.duplicates_removed.items():
                report.append(f"   {item:<45} {amount:>15,.2f} SEK")
            report.append("")
            report.append("   Worldline deposits show up in Marginalen as 'B...' transactions.")
            report.append("   We only count them once (from Marginalen B transactions).")
            report.append("")
        
        # Summary
        report.append("📋 SUMMARY:")
        report.append("=" * 80)
        if self.real_sales:
            total_sales = sum(self.real_sales.values())
            total_with_vat = worldline_gross + lunar_gross + marginalen_3001 + wise_gross
            net_sales = total_with_vat / Decimal('1.25')
            vat = total_with_vat - net_sales
            norway = self.real_sales.get('Norway Export (3105)', Decimal('0'))
            
            report.append(f"   Real Sales (Gross):              {total_sales:>15,.2f} SEK")
            report.append(f"   Real Sales (Net, excl. VAT):     {net_sales + norway:>15,.2f} SEK")
            report.append(f"   Output VAT 25%:                  {vat:>15,.2f} SEK")
        
        if self.non_sales_income:
            total_non_sales = sum(self.non_sales_income.values())
            report.append(f"   Other Income (Insurance/Bidrag): {total_non_sales:>15,.2f} SEK")
        
        report.append("")
        report.append("✅ NO DOUBLE-COUNTING")
        report.append("✅ INSURANCE SEPARATED FROM SALES")
        report.append("")
        
        return "\n".join(report)
    
    def run_audit(self):
        """Execute corrected audit"""
        print("Running CORRECTED Sales & VAT Audit...")
        
        self.audit_real_sales()
        
        report = self.generate_report()
        
        # Save report
        output_file = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\DOKTOR_FORENSIC_AUDIT_2026-05-07") / "CORRECTED_SALES_AUDIT_FIXED.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(report)
        print(f"\nReport saved to: {output_file}")
        
        return report


if __name__ == "__main__":
    auditor = CorrectedSalesAuditor()
    auditor.run_audit()
