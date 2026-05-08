import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal

p = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03\source_csv\worldline\WORLDLINE_STANDALONE.se')
vers = parse_se_file(p)

# Sum all 1947 movements
total_1947 = Decimal('0')
sales_1947 = Decimal('0')
fees_1947 = Decimal('0')
other_1947 = Decimal('0')
for v in vers:
    for acc, amt in v['trans']:
        if acc == '1947':
            total_1947 += amt
            if 'FEE' in v['desc'].upper():
                fees_1947 += amt
            elif any(a in ('3001', '3051', '3105') for a, _ in v['trans']):
                sales_1947 += amt
            else:
                other_1947 += amt
                print(f"OTHER: {v['ver']} {v['date']} {v['desc'][:60]} 1947={amt}")

print(f"Total 1947 net movement (Worldline source): {total_1947:.2f}")
print(f"  Sales (debits to 1947):  {sales_1947:.2f}")
print(f"  Fees  (credits to 1947): {fees_1947:.2f}")
print(f"  Other:                   {other_1947:.2f}")
print(f"  Net 1947 balance change: {total_1947:.2f}")
print()
print(f"Marginalen B-trans (deposits): 194,159.97")
print(f"Diff (should be ~zero if all transfers covered): {Decimal('194159.97') - total_1947:.2f}")
