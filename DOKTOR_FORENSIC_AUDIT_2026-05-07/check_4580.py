import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
vers = parse_se_file(Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03\MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'))
print('=== Account 4580 (freight/customs) movements ===')
for v in vers:
    has = any(acc == '4580' for acc, _ in v['trans'])
    if has:
        print(f"\n  {v['ver']} {v['date']}  {v['desc'][:80]}")
        for a, amt in v['trans']:
            print(f'      {a}: {amt}')
