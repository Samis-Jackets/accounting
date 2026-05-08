"""Find import VAT issue - boxes 60-62 require box 50.
Account mapping (BAS):
  Box 50 (import value):       4545 (25%), 4546 (12%), 4547 (6%)
  Box 60 (import VAT 25%):     2615
  Box 61 (import VAT 12%):     2625
  Box 62 (import VAT 6%):      2635
  Box 48 (input VAT on import deductible): 2645
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

import_accs = ['4545', '4546', '4547', '4515', '4516', '4517',
               '2615', '2625', '2635', '2645',
               '4531', '4532', '4533',  # EU acquisition
               '2614', '2624', '2634',  # EU acquisition VAT
               '2641', '2642', '2640']  # input VAT

print('Movements on IMPORT/EU-VAT accounts:')
print('-' * 90)
sums = defaultdict(Decimal)
movements = defaultdict(list)
for v in vers:
    for acc, amt in v['trans']:
        if acc in import_accs:
            sums[acc] += amt
            movements[acc].append((v['ver'], v['date'], amt, v['desc'][:60]))

for acc in sorted(sums.keys()):
    print(f'\n  Account {acc}: net = {sums[acc]:.2f}')
    for m in movements[acc][:10]:
        print(f'    {m[0]} {m[1]}  {m[2]:>10.2f}  {m[3]}')
    if len(movements[acc]) > 10:
        print(f'    ... and {len(movements[acc])-10} more')

print()
print('=' * 90)
print('IMPORT VAT REPORT BOXES (Q1 2026)')
print('=' * 90)
box60 = -sums['2615']  # output import VAT 25% (credit balance)
box61 = -sums['2625']
box62 = -sums['2635']
box50_25 = sums['4545']  # import value 25% (debit balance)
box50_12 = sums['4546']
box50_06 = sums['4547']
box48 = sums['2645']  # deductible input VAT on import

print(f'  Box 60 (Output VAT import 25%): {box60:>10.2f}')
print(f'  Box 61 (Output VAT import 12%): {box61:>10.2f}')
print(f'  Box 62 (Output VAT import 6%):  {box62:>10.2f}')
print(f'  Box 50 (Import value 25%, 4545): {box50_25:>10.2f}')
print(f'  Box 50 (Import value 12%, 4546): {box50_12:>10.2f}')
print(f'  Box 50 (Import value 6%,  4547): {box50_06:>10.2f}')
print(f'  TOTAL Box 50 (import value):     {box50_25+box50_12+box50_06:>10.2f}')
print(f'  Box 48 (input VAT 2645):         {box48:>10.2f}')

print()
if box60 + box61 + box62 > 0 and (box50_25+box50_12+box50_06) == 0:
    print('[PROBLEM CONFIRMED]')
    print(f'   Output import VAT booked: {box60+box61+box62:.2f}')
    print(f'   But import VALUE on 4545/4546/4547: 0.00 -> Box 50 is empty!')
    print(f'   FIX: Box 50 must equal sum of underlying values that generated boxes 60-62')
    print(f'   Computed Box 50 from VAT: 25% basis = {box60*4:.2f}, 12%={box61/Decimal("0.12"):.2f}, 6%={box62/Decimal("0.06") if box62 else 0:.2f}')
