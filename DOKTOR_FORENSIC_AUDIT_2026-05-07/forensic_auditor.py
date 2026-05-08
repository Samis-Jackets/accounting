"""
FORENSIC AUDIT ANALYZER - SAMIS JACKETS AB
Automated transaction analysis with rule-based checking
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Transaction:
    series: str
    number: int
    date: str
    description: str
    entries: List[Tuple[str, float]]  # [(account, amount), ...]
    
@dataclass
class Finding:
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    transaction: str  # VER reference
    rule: str
    issue: str
    recommendation: str

class ForensicAuditor:
    """
    Audits SE file transactions against Swedish accounting rules
    """
    
    def __init__(self):
        self.findings = []
        self.stats = {
            'total_transactions': 0,
            'clean': 0,
            'issues': 0,
            'by_severity': {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
        }
        
        # Account classification rules (from ACCOUNTING_METHODOLOGY)
        self.rules = {
            # Bank accounts
            'bank_accounts': ['1930', '1940', '1941', '1942', '1943', '1944', '1945', '1947', '1948'],
            # Revenue accounts
            'revenue_domestic': '3051',  # 25% VAT
            'revenue_export': '3105',     # 0% VAT
            'revenue_other': ['3001', '3190'],
            # Cost accounts
            'inventory': '1460',
            'cogs': '4110',
            'consumables': '5460',
            'rent': '5010',
            'bank_fees': '6570',
            # Related party
            'related_party': '2893',
            # VAT accounts
            'vat_out': '2611',  # Output VAT
            'vat_in': '2641',   # Input VAT
            'vat_import_deduct': '2645',
            'vat_import_pay': '2615',
        }
        
    def parse_se_file(self, filepath: str) -> List[Transaction]:
        """Parse SE file and extract all transactions"""
        transactions = []
        
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
            
        # Find all VER blocks
        ver_pattern = r'#VER ([A-Z]+) (\d+) (\d{8}) "(.*?)".*?\{(.*?)\}'
        matches = re.findall(ver_pattern, content, re.DOTALL)
        
        for match in matches:
            series, number, date, desc, trans_block = match
            
            # Extract TRANS lines
            trans_pattern = r'#TRANS (\d+) \{\} (-?\d+(?:\.\d+)?)'
            trans_entries = re.findall(trans_pattern, trans_block)
            
            entries = [(acc, float(amt)) for acc, amt in trans_entries]
            
            transactions.append(Transaction(
                series=series,
                number=int(number),
                date=date,
                description=desc,
                entries=entries
            ))
            
        return transactions
    
    def check_balance(self, trans: Transaction) -> bool:
        """Verify debits equal credits"""
        total = sum(amt for _, amt in trans.entries)
        return abs(total) < 0.01  # Allow for rounding
    
    def check_vat_on_sales(self, trans: Transaction) -> List[Finding]:
        """Check if sales have proper VAT"""
        findings = []
        
        has_3051 = any(acc == '3051' for acc, _ in trans.entries)
        has_3105 = any(acc == '3105' for acc, _ in trans.entries)
        has_vat_2611 = any(acc == '2611' for acc, _ in trans.entries)
        
        if has_3051 and not has_vat_2611:
            findings.append(Finding(
                severity='HIGH',
                transaction=f"{trans.series} {trans.number}",
                rule='VAT Law §3 - Domestic sales require 25% VAT',
                issue=f'Account 3051 used without VAT account 2611',
                recommendation='Add VAT entry: K 2611 (25% of 3051 amount)'
            ))
        
        if has_3105 and has_vat_2611:
            findings.append(Finding(
                severity='MEDIUM',
                transaction=f"{trans.series} {trans.number}",
                rule='VAT Law §5 - Export sales are zero-rated',
                issue=f'Account 3105 (export) should not have VAT',
                recommendation='Remove 2611 VAT entry for export sales'
            ))
            
        return findings
    
    def check_private_business_separation(self, trans: Transaction) -> List[Finding]:
        """Check for proper private/business separation"""
        findings = []
        
        # Keywords indicating private expenses
        private_keywords = ['mat', 'food', 'ica', 'willys', 'coop', 'lidl', 'lunch', 
                          'middag', 'frukost', 'dinner', 'breakfast']
        
        desc_lower = trans.description.lower()
        has_private_keyword = any(kw in desc_lower for kw in private_keywords)
        uses_2893 = any(acc == '2893' for acc, _ in trans.entries)
        uses_business_cost = any(acc.startswith(('4', '5', '6', '7')) for acc, _ in trans.entries)
        
        if has_private_keyword and uses_business_cost and not uses_2893:
            findings.append(Finding(
                severity='CRITICAL',
                transaction=f"{trans.series} {trans.number}",
                rule='BFL 5§ - Private expenses cannot be deducted',
                issue=f'Potential private expense: "{trans.description}"',
                recommendation='Either remove entry or reclassify to 2893 (related party)'
            ))
            
        return findings
    
    def check_inventory_classification(self, trans: Transaction) -> List[Finding]:
        """Check for proper inventory vs consumables classification"""
        findings = []
        
        # Check for large 5460 amounts (potential misclassification like Finding #001)
        for acc, amt in trans.entries:
            if acc == '5460' and amt > 50000:
                findings.append(Finding(
                    severity='HIGH',
                    transaction=f"{trans.series} {trans.number}",
                    rule='ÅRL 4 kap. 9§ - Inventory valuation',
                    issue=f'Large amount {amt:.2f} SEK to 5460 (consumables) - should this be inventory 1460?',
                    recommendation='Review if this should be capitalized to 1460 instead of expensed'
                ))
                
        # Check for inventory purchases with VAT (should use reverse charge for imports)
        has_1460 = any(acc == '1460' for acc, _ in trans.entries)
        has_2641_vat = any(acc == '2641' and amt > 10000 for acc, amt in trans.entries)
        
        if has_1460 and has_2641_vat:
            findings.append(Finding(
                severity='MEDIUM',
                transaction=f"{trans.series} {trans.number}",
                rule='Import VAT - Reverse charge required for large imports',
                issue='Large inventory import may need reverse charge (2645/2615) instead of regular VAT (2641)',
                recommendation='Verify if this is import or domestic purchase'
            ))
            
        return findings
    
    def check_account_exists(self, trans: Transaction) -> List[Finding]:
        """Check for unusual or non-standard accounts"""
        findings = []
        
        standard_accounts = set(['1220', '1240', '1460', '1580', '1630', '1910', '1930', '1940', '1941', 
                                '1942', '1943', '1944', '1945', '1947', '1948', '2091', '2093', '2098',
                                '2441', '2448', '2510', '2611', '2615', '2641', '2645', '2650', '2710',
                                '2731', '2893', '3001', '3051', '3105', '3190', '3985', '3994', '4110',
                                '4580', '5010', '5410', '5420', '5460', '5611', '5700', '5710', '5800',
                                '5900', '6212', '6310', '6500', '6570', '7210', '7510', '7960', '8311',
                                '8423'])
        
        for acc, _ in trans.entries:
            if acc not in standard_accounts:
                findings.append(Finding(
                    severity='LOW',
                    transaction=f"{trans.series} {trans.number}",
                    rule='Chart of Accounts - EU-BAS97',
                    issue=f'Unusual account {acc} not in standard list',
                    recommendation='Verify account is valid and properly defined'
                ))
                
        return findings
    
    def audit_transaction(self, trans: Transaction) -> List[Finding]:
        """Run all audit checks on a transaction"""
        findings = []
        
        # Check 1: Balance
        if not self.check_balance(trans):
            findings.append(Finding(
                severity='CRITICAL',
                transaction=f"{trans.series} {trans.number}",
                rule='BFL 5 kap. 1§ - Double-entry bookkeeping',
                issue='Transaction does not balance (debits ≠ credits)',
                recommendation='Review and correct entry'
            ))
        
        # Check 2: VAT on sales
        findings.extend(self.check_vat_on_sales(trans))
        
        # Check 3: Private/business separation
        findings.extend(self.check_private_business_separation(trans))
        
        # Check 4: Inventory classification
        findings.extend(self.check_inventory_classification(trans))
        
        # Check 5: Account validity
        findings.extend(self.check_account_exists(trans))
        
        return findings
    
    def audit_batch(self, transactions: List[Transaction], batch_num: int) -> Dict:
        """Audit a batch of transactions"""
        batch_findings = []
        clean_count = 0
        
        for trans in transactions:
            trans_findings = self.audit_transaction(trans)
            
            if trans_findings:
                batch_findings.extend(trans_findings)
                self.stats['issues'] += 1
            else:
                clean_count += 1
                self.stats['clean'] += 1
                
            self.stats['total_transactions'] += 1
        
        # Update severity stats
        for finding in batch_findings:
            self.stats['by_severity'][finding.severity] += 1
        
        return {
            'batch': batch_num,
            'transactions_audited': len(transactions),
            'clean': clean_count,
            'with_issues': len(transactions) - clean_count,
            'findings': batch_findings
        }
    
    def generate_batch_report(self, batch_result: Dict) -> str:
        """Generate markdown report for a batch"""
        report = f"""# BATCH {batch_result['batch']:02d} AUDIT REPORT

**Transactions Audited:** {batch_result['transactions_audited']}  
**Clean Transactions:** {batch_result['clean']}  
**Transactions with Issues:** {batch_result['with_issues']}  
**Total Findings:** {len(batch_result['findings'])}

---

## FINDINGS

"""
        
        if not batch_result['findings']:
            report += "✅ **NO ISSUES FOUND** - All transactions comply with accounting rules.\n\n"
        else:
            # Group by severity
            by_severity = {}
            for finding in batch_result['findings']:
                if finding.severity not in by_severity:
                    by_severity[finding.severity] = []
                by_severity[finding.severity].append(finding)
            
            for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
                if severity in by_severity:
                    findings_list = by_severity[severity]
                    icon = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '🟢'}[severity]
                    
                    report += f"### {icon} {severity} SEVERITY ({len(findings_list)} findings)\n\n"
                    
                    for i, finding in enumerate(findings_list, 1):
                        report += f"""#### {i}. {finding.transaction}

**Rule:** {finding.rule}  
**Issue:** {finding.issue}  
**Recommendation:** {finding.recommendation}

---

"""
        
        return report


if __name__ == "__main__":
    print("Forensic Auditor Ready")
    print("Usage:")
    print("  auditor = ForensicAuditor()")
    print("  transactions = auditor.parse_se_file('path/to/file.se')")
    print("  result = auditor.audit_batch(transactions[0:50], 1)")
    print("  report = auditor.generate_batch_report(result)")
