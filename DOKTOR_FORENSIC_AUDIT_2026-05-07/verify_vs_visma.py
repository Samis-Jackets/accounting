"""Verify NET (credits - debits) for sales accounts vs Visma."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal
from collections import defaultdict

BASE = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip')
MASTER = BASE / 'Q1_2026_PERIOD_2026-01_TO_2026-03' / 'MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'

vers = parse_se_file(MASTER)

acc_credit = defaultdict(Decimal)  # negative amounts (credits) -> stored positive
acc_debit = defaultdict(Decimal)   # positive amounts (debits)

for v in vers:
    for acc, amt in v['trans']:
        if amt < 0:
            acc_credit[acc] += -amt
        else:
            acc_debit[acc] += amt

print('=' * 70)
print('VISMA REPORTED vs MASTER (NET = Credits - Debits)')
print('=' * 70)

def show(acc, label, visma):
    cr = acc_credit[acc]
    dr = acc_debit[acc]
    net = cr - dr
    diff = net - Decimal(str(visma))
    flag = '[OK]' if abs(diff) < Decimal('1') else '[DIFF]'
    print(f'  {acc} {label:35s} cr={cr:>10.2f} dr={dr:>8.2f} NET={net:>10.2f}  Visma={visma:>10.2f}  {flag} {diff:+.2f}')

print()
print('--- 25% VAT SALES ---')
show('3001', 'Sales 25% VAT', 0)  # placeholder
show('3051', 'Sales 25% VAT (alt)', 0)
total_25_net = (acc_credit['3001'] - acc_debit['3001']) + (acc_credit['3051'] - acc_debit['3051'])
print(f'  TOTAL 25% NET: {total_25_net:.2f}    Visma: 261,313.00    diff: {total_25_net - Decimal("261313"):+.2f}')

print()
print('--- VAT 2611 ---')
show('2611', 'Output VAT 25%', 65328)

print()
print('--- 0% VAT SALES ---')
show('3105', 'Export 0% VAT', 58000)

print()
print('--- BANK ACCOUNTS (sales receipts only) ---')
# For Lunar/Wise/Worldline, also compute net of refunds
sales_by_bank = defaultdict(lambda: {'cr': Decimal('0'), 'dr': Decimal('0')})
for v in vers:
    has_sale_credit = any(acc in ('3001', '3051', '3105', '3190') and amt < 0 for acc, amt in v['trans'])
    has_sale_debit = any(acc in ('3001', '3051', '3105', '3190') and amt > 0 for acc, amt in v['trans'])
    for acc, amt in v['trans']:
        if acc in ('1910', '1930', '1944', '1947', '1948'):
            if has_sale_credit and amt > 0:
                sales_by_bank[acc]['dr'] += amt
            elif has_sale_debit and amt < 0:
                sales_by_bank[acc]['cr'] += -amt

for bank, d in sales_by_bank.items():
    net = d['dr'] - d['cr']
    print(f'  {bank}: deposits={d["dr"]:>10.2f}, refunds={d["cr"]:>8.2f}, NET sales receipts={net:>10.2f}')

print()
print('=' * 70)
total_visma = Decimal('261313') + Decimal('65328') + Decimal('58000')
total_master_net_sales = total_25_net + (acc_credit['2611'] - acc_debit['2611']) + (acc_credit['3105'] - acc_debit['3105'])
print(f'TOTAL Visma gross:   {total_visma:>12.2f}')
print(f'TOTAL Master gross:  {total_master_net_sales:>12.2f}')
print(f'DIFF:                {total_master_net_sales - total_visma:>+12.2f}')
