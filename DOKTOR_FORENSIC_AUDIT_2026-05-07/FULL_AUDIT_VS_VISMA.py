"""Full sales audit vs Visma reported totals.
Visma says: 261,313 net (25% VAT) + 65,328 VAT + 58,000 (0% VAT) = 384,641 gross
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal
from collections import defaultdict

BASE = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip')
MASTER = BASE / 'Q1_2026_PERIOD_2026-01_TO_2026-03' / 'MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'

vers = parse_se_file(MASTER)
print(f'Total VERs in master: {len(vers)}')

# Sum movements per account
acc_sums = defaultdict(Decimal)
for v in vers:
    for acc, amt in v['trans']:
        acc_sums[acc] += amt

print()
print('=== SALES ACCOUNTS (credits = negative sums) ===')
for acc in ['3001', '3051', '3105', '3190', '3740', '3994', '3985', '3960', '3970']:
    if acc in acc_sums:
        print(f'  {acc}: {-acc_sums[acc]:>12.2f}  (credit balance)')

print()
print('=== VAT ACCOUNT 2611 ===')
print(f'  2611: {-acc_sums["2611"]:>12.2f}  (credit balance = output VAT)')

print()
print('=== BANK ACCOUNTS (debit balance for receipts) ===')
for acc in ['1910', '1930', '1944', '1947', '1948']:
    if acc in acc_sums:
        print(f'  {acc}: {acc_sums[acc]:>12.2f}')

# Visma expected
print()
print('=== VISMA REPORTED ===')
print(f'  Net 25% VAT sales:  261,313.00')
print(f'  Output VAT 25%:      65,328.00  (=261,313*0.25 = {261313*0.25:.2f})')
print(f'  0% VAT sales:        58,000.00')
print(f'  Total gross:        384,641.00')

# Compute master totals
sales_25 = Decimal('0')  # 3001
sales_0 = Decimal('0')   # 3105 (export Norway typically)
sales_other = defaultdict(Decimal)

for v in vers:
    has_2611 = any(acc == '2611' for acc, _ in v['trans'])
    for acc, amt in v['trans']:
        if acc.startswith('30') or acc.startswith('31'):
            if amt < 0:  # credit = sale
                if acc == '3001':
                    sales_25 += -amt
                elif acc in ('3105', '3051'):
                    sales_0 += -amt
                else:
                    sales_other[acc] += -amt

print()
print('=== MASTER COMPUTED ===')
print(f'  3001 (25% VAT sales net):  {sales_25:>12.2f}')
print(f'  3051+3105 (0% sales):       {sales_0:>12.2f}')
print(f'  Other 30xx/31xx:')
for acc, amt in sales_other.items():
    print(f'    {acc}: {amt:.2f}')
print(f'  2611 VAT (credit):          {-acc_sums["2611"]:>12.2f}')

print()
print('=== DIFFS (Master - Visma) ===')
print(f'  3001 net:  {sales_25 - Decimal("261313"):>+12.2f}')
print(f'  VAT 2611:  {-acc_sums["2611"] - Decimal("65328"):>+12.2f}')
print(f'  3105/3051: {sales_0 - Decimal("58000"):>+12.2f}')
