#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DOKTOR SALES & VAT AUDIT ANALYZER
Samis Jackets AB - Org.nr: 559489-5301
Date: 2026-05-07

PURPOSE: Identify missing sales and VAT discrepancies
"""

import re
from pathlib import Path
from decimal import Decimal

class SalesVATAuditor:
    """Audit sales and VAT across all sources"""
    
    def __init__(self):
        self.findings = []
        self.missing_sales = {}
        self.missing_vat = {}
        self.rent_vat_issues = []
        
    def extract_res_balance(self, se_file_path, account):
        """Extract #RES balance for an account from SE file"""
        try:
            with open(se_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Pattern: #RES 0 ACCOUNT AMOUNT
            pattern = rf'#RES\s+0\s+{account}\s+([-\d.]+)'
            matches = re.findall(pattern, content)
            
            if matches:
                # Return the absolute value (sales are negative)
                return abs(Decimal(matches[0]))
            return Decimal('0')
        except Exception as e:
            print(f"Error reading {se_file_path}: {e}")
            return Decimal('0')
    
    def audit_standalone_files(self):
        """Check standalone SE files vs main ledger"""
        
        base_path = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
        
        # LUNAR BANK
        lunar_file = base_path / "source_csv" / "Lunar Bank" / "LUNAR_STANDALONE.se"
        lunar_sales = self.extract_res_balance(lunar_file, "3001")
        if lunar_sales > 0:
            self.missing_sales['Lunar Bank (3001)'] = lunar_sales
            # Calculate VAT: sales are gross, need to extract 25%
            net_sales = lunar_sales / Decimal('1.25')
            vat = lunar_sales - net_sales
            self.missing_vat['Lunar Bank VAT (2611)'] = vat
        
        # WORLDLINE
        worldline_file = base_path / "source_csv" / "worldline" / "WORLDLINE_STANDALONE.se"
        worldline_sales = self.extract_res_balance(worldline_file, "3051")
        if worldline_sales > 0:
            self.missing_sales['Worldline (3051)'] = worldline_sales
            # Calculate VAT
            net_sales = worldline_sales / Decimal('1.25')
            vat = worldline_sales - net_sales
            self.missing_vat['Worldline VAT (2611)'] = vat
        
        # WISE EU/USD
        wise_file = base_path / "source_csv" / "wise" / "usd" / "20260101-20261231.se"
        wise_sales = self.extract_res_balance(wise_file, "3051")
        if wise_sales > 0:
            self.missing_sales['Wise EU/USD (3051)'] = wise_sales
            # Calculate VAT
            net_sales = wise_sales / Decimal('1.25')
            vat = wise_sales - net_sales
            self.missing_vat['Wise VAT (2611)'] = vat
        
        # NORWAY EXPORTS
        marginalen_file = base_path / "source_csv" / "marginalen" / "MARGINALEN_STANDALONE.se"
        norway_sales = self.extract_res_balance(marginalen_file, "3105")
        if norway_sales > 0:
            # Check if already in main ledger
            main_ledger = base_path / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
            main_norway = self.extract_res_balance(main_ledger, "3105")
            if main_norway == 0:
                self.missing_sales['Norway Export (3105)'] = norway_sales
                # No VAT on exports (0%)
        
    def check_main_ledger_totals(self):
        """Get current main ledger totals"""
        base_path = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
        main_ledger = base_path / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
        
        current_3051 = self.extract_res_balance(main_ledger, "3051")
        current_3001 = self.extract_res_balance(main_ledger, "3001")
        current_3105 = self.extract_res_balance(main_ledger, "3105")
        
        return {
            '3051': current_3051,
            '3001': current_3001,
            '3105': current_3105
        }
    
    def check_rent_vat(self):
        """Check if VAT was incorrectly claimed on rent"""
        # Read main ledger for rent transactions with VAT
        base_path = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
        main_ledger = base_path / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
        
        try:
            with open(main_ledger, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find VER entries with rent (5010) and VAT (2641)
            ver_pattern = r'#VER\s+\w+\s+(\d+)\s+(\d{8})\s+"([^"]*)"[^{]*\{([^}]+)\}'
            vers = re.findall(ver_pattern, content, re.DOTALL)
            
            for ver_num, date, desc, trans_block in vers:
                # Check if this VER has both 5010 (rent) and 2641 (input VAT)
                has_rent = '5010' in trans_block
                has_vat = '2641' in trans_block
                
                if has_rent and has_vat:
                    # Extract amounts
                    rent_match = re.search(r'#TRANS\s+5010\s+\{\}\s+([\d.]+)', trans_block)
                    vat_match = re.search(r'#TRANS\s+2641\s+\{\}\s+([\d.]+)', trans_block)
                    
                    if rent_match and vat_match:
                        rent_amount = Decimal(rent_match.group(1))
                        vat_amount = Decimal(vat_match.group(1))
                        
                        self.rent_vat_issues.append({
                            'ver': ver_num,
                            'date': date,
                            'desc': desc,
                            'rent': rent_amount,
                            'vat': vat_amount
                        })
        except Exception as e:
            print(f"Error checking rent VAT: {e}")
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        
        report = []
        report.append("=" * 80)
        report.append("DOKTOR FORENSIC AUDIT - SALES & VAT DISCREPANCIES")
        report.append("Samis Jackets AB - Org.nr: 559489-5301")
        report.append("Date: 2026-05-07")
        report.append("Period: Q1 2026 (2026-01-01 to 2026-03-31)")
        report.append("=" * 80)
        report.append("")
        
        # Current ledger status
        current = self.check_main_ledger_totals()
        report.append("📊 CURRENT MAIN LEDGER (Q1 2026):")
        report.append(f"   Account 3051 (Sweden 25% VAT): {current['3051']:,.2f} SEK")
        report.append(f"   Account 3001 (Sales 25% VAT):  {current['3001']:,.2f} SEK")
        report.append(f"   Account 3105 (Export 0% VAT):  {current['3105']:,.2f} SEK")
        report.append(f"   TOTAL RECORDED SALES: {sum(current.values()):,.2f} SEK")
        report.append("")
        
        # Missing sales
        if self.missing_sales:
            report.append("🔴 CRITICAL: MISSING SALES NOT IN MAIN LEDGER")
            report.append("-" * 80)
            total_missing = Decimal('0')
            for source, amount in self.missing_sales.items():
                report.append(f"   {source:<35} {amount:>15,.2f} SEK")
                total_missing += amount
            report.append("-" * 80)
            report.append(f"   {'TOTAL MISSING SALES':<35} {total_missing:>15,.2f} SEK")
            report.append("")
        
        # Missing VAT
        if self.missing_vat:
            report.append("🔴 CRITICAL: MISSING UTGÅENDE MOMS (OUTPUT VAT)")
            report.append("-" * 80)
            total_missing_vat = Decimal('0')
            for source, amount in self.missing_vat.items():
                report.append(f"   {source:<35} {amount:>15,.2f} SEK")
                total_missing_vat += amount
            report.append("-" * 80)
            report.append(f"   {'TOTAL MISSING VAT':<35} {total_missing_vat:>15,.2f} SEK")
            report.append("")
        
        # Rent VAT issues
        if self.rent_vat_issues:
            report.append("🔴 CRITICAL: INCORRECT INPUT VAT ON RENT")
            report.append("-" * 80)
            report.append("   Commercial rent is typically VAT-exempt in Sweden.")
            report.append("   Input VAT should not be claimed unless landlord charged VAT.")
            report.append("")
            total_incorrect_vat = Decimal('0')
            for issue in self.rent_vat_issues:
                report.append(f"   VER {issue['ver']} ({issue['date']}): {issue['desc']}")
                report.append(f"      Rent: {issue['rent']:,.2f} SEK | Input VAT: {issue['vat']:,.2f} SEK")
                total_incorrect_vat += issue['vat']
            report.append("-" * 80)
            report.append(f"   {'TOTAL INCORRECT VAT TO REVERSE':<35} {total_incorrect_vat:>15,.2f} SEK")
            report.append("")
        
        # Financial impact
        report.append("💰 FINANCIAL IMPACT SUMMARY")
        report.append("=" * 80)
        
        if self.missing_sales:
            total_missing_sales = sum(self.missing_sales.values())
            report.append(f"   Sales understated by:        {total_missing_sales:>15,.2f} SEK")
        
        if self.missing_vat:
            total_missing_vat = sum(self.missing_vat.values())
            report.append(f"   Output VAT understated by:   {total_missing_vat:>15,.2f} SEK")
        
        if self.rent_vat_issues:
            total_incorrect_vat = sum(issue['vat'] for issue in self.rent_vat_issues)
            report.append(f"   Input VAT overstated by:     {total_incorrect_vat:>15,.2f} SEK")
            report.append(f"   Net VAT liability increase:  {total_missing_vat - total_incorrect_vat:>15,.2f} SEK")
        
        report.append("")
        
        # Recommendations
        report.append("✅ RECOMMENDATIONS")
        report.append("=" * 80)
        report.append("1. Import standalone SE files for Lunar, Worldline, and Wise")
        report.append("2. Reverse incorrect input VAT on rent (if applicable)")
        report.append("3. File corrected VAT return if previously filed")
        report.append("4. Update financial statements with corrected sales figures")
        report.append("")
        
        return "\n".join(report)
    
    def run_full_audit(self):
        """Execute complete audit"""
        print("Starting Sales & VAT Audit...")
        
        self.audit_standalone_files()
        self.check_rent_vat()
        
        report = self.generate_report()
        
        # Save report
        output_file = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\DOKTOR_FORENSIC_AUDIT_2026-05-07") / "SALES_VAT_AUDIT_REPORT.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(report)
        print(f"\nReport saved to: {output_file}")
        
        return report


if __name__ == "__main__":
    auditor = SalesVATAuditor()
    auditor.run_full_audit()
