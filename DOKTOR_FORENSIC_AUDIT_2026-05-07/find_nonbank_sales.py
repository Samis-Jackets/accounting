"""Find sale VERs without bank accounts - these are the missing pieces."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal

BASE = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip')
MASTER = BASE / 'Q1_2026_PERIOD_2026-01_TO_2026-03' / 'MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'
vers = parse_se_file(MASTER)

banks = {'1947', '1944', '1948', '1930', '1910'}

print('Sale VERs WITHOUT a bank account (refunds, contra, accruals):')
print('-' * 90)
total_25_net = Decimal('0')
total_vat = Decimal('0')
for v in vers:
    has_bank = any(acc in banks for acc, _ in v['trans'])
    has_sale_acc = any(acc in ('3001', '3051', '3105', '2611') for acc, _ in v['trans'])
    if has_sale_acc and not has_bank:
        s25 = sum(amt for acc, amt in v['trans'] if acc in ('3001', '3051'))
        vat = sum(amt for acc, amt in v['trans'] if acc == '2611')
        total_25_net += -s25
        total_vat += -vat
        accs = ' '.join(f'{a}={amt}' for a,amt in v['trans'])
        print(f"  {v['ver']} {v['date']}  {v['desc'][:40]:40s}  {accs}")

print('-' * 90)
print(f'Total non-bank 25% net: {total_25_net:.2f}')
print(f'Total non-bank VAT:     {total_vat:.2f}')
