"""Check ALL accounts with movement that could trigger box 50 or 60-62 in Visma."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from collections import defaultdict
from decimal import Decimal

vers = parse_se_file(Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03\MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'))

# Visma auto-mapping (BAS standard) for MOMS boxes:
# Box 20: 4515 (EU goods 25% basis)
# Box 21: 4516 (EU goods 12% basis)
# Box 22: 4517 (EU goods 6% basis)
# Box 30: 2614 (EU goods VAT 25%)
# Box 31: 2624 (EU goods VAT 12%)
# Box 32: 2634 (EU goods VAT 6%)
# Box 23: 4518 (EU services 25%)
# Box 24: 4531 (services from non-EU 25%) / 4535 (EU)
# Box 50: 4545 (import 25%), 4546, 4547
# Box 60: 2615 (output VAT import 25%)
# Box 61: 2625
# Box 62: 2635
# Box 48: 2640/2645/2641 (input VAT)

mapping = {
    '4515': 'Box 20', '4516': 'Box 21', '4517': 'Box 22',
    '2614': 'Box 30', '2624': 'Box 31', '2634': 'Box 32',
    '4518': 'Box 23',
    '4531': 'Box 24', '4532': 'Box 24', '4533': 'Box 24', '4535': 'Box 24',
    '4545': 'Box 50 (25%)', '4546': 'Box 50 (12%)', '4547': 'Box 50 (6%)',
    '2615': 'Box 60', '2625': 'Box 61', '2635': 'Box 62',
    '2640': 'Box 48', '2641': 'Box 48', '2645': 'Box 48',
    '2647': 'Box 48',
}

sums = defaultdict(Decimal)
for v in vers:
    for acc, amt in v['trans']:
        sums[acc] += amt

print('=== ALL accounts with movement that map to MOMS report boxes ===')
for acc in sorted(mapping.keys()):
    if sums[acc] != 0:
        print(f'  {acc} ({mapping[acc]}): {sums[acc]:.2f}')

print()
print('=== ALL non-zero accounts in 2600-2699 (VAT) range ===')
for acc in sorted(sums.keys()):
    if acc.startswith('26') and sums[acc] != 0:
        print(f'  {acc}: {sums[acc]:.2f}')

print()
print('=== ALL non-zero accounts in 4500-4599 (purchase) range ===')
for acc in sorted(sums.keys()):
    if acc.startswith('45') and sums[acc] != 0:
        print(f'  {acc}: {sums[acc]:.2f}')

print()
print('=== ALL non-zero accounts in 4600-4799 (services from foreign) range ===')
for acc in sorted(sums.keys()):
    if (acc.startswith('46') or acc.startswith('47')) and sums[acc] != 0:
        print(f'  {acc}: {sums[acc]:.2f}')
