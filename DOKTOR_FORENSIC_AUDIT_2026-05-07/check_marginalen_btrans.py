import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal

# Read Marginalen standalone for B-trans
mp = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03\source_csv\marginalen\MARGINALEN_STANDALONE.se')
mvers = parse_se_file(mp)

# Find Worldline-related deposits - typically credited 1947 or "B-trans" descriptions
# Per the audit, "Marginalen B-trans (Worldline deposits): 194,159.97"
# These come into 1930 and balance to 1947
btrans = []
for v in mvers:
    desc = v['desc'].upper()
    # Worldline deposits: debit 1930, credit 1947
    has_1930_debit = any(acc == '1930' and amt > 0 for acc, amt in v['trans'])
    has_1947 = any(acc == '1947' for acc, amt in v['trans'])
    if has_1930_debit and has_1947:
        amt = sum(amt for acc, amt in v['trans'] if acc == '1930' and amt > 0)
        btrans.append((v['ver'], v['date'], v['desc'], amt))

print(f"Marginalen Worldline deposits (B-trans): {len(btrans)}")
total = sum(b[3] for b in btrans)
print(f"Total: {total:.2f}")
print()
print("Last 10 deposits:")
for b in btrans[-10:]:
    print(f"  {b[0]} {b[1]} {b[3]:>10.2f}  {b[2][:60]}")
print()
print("After 20260330:")
for b in btrans:
    if b[1] > '20260330':
        print(f"  {b[0]} {b[1]} {b[3]:>10.2f}  {b[2][:60]}")
