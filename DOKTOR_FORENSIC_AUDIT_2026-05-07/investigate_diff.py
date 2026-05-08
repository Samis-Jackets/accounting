"""Investigate 3001 vs 3051 split and find the 2,420 discrepancy."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file
from pathlib import Path
from decimal import Decimal
from collections import defaultdict

BASE = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip')
MASTER = BASE / 'Q1_2026_PERIOD_2026-01_TO_2026-03' / 'MASTER_Q1_2026_CORRECTED_CASH_BASIS.se'

vers = parse_se_file(MASTER)

# For each sale VER, check VAT ratio
print('=== ANALYZING VAT RATIO PER VER ===')
no_vat = []
correct_25 = []
weird = []

# Group by bank account too
by_bank = defaultdict(lambda: {'net': Decimal('0'), 'vat': Decimal('0'), 'count': 0})

for v in vers:
    sale_net = Decimal('0')
    vat = Decimal('0')
    bank_acc = None
    for acc, amt in v['trans']:
        if acc in ('3001', '3051') and amt < 0:
            sale_net += -amt
        elif acc == '2611':
            vat += -amt
        elif acc in ('1910', '1930', '1944', '1947', '1948') and amt > 0:
            bank_acc = acc

    if sale_net == 0:
        continue

    if bank_acc:
        by_bank[bank_acc]['net'] += sale_net
        by_bank[bank_acc]['vat'] += vat
        by_bank[bank_acc]['count'] += 1

    if vat == 0:
        no_vat.append((v['ver'], v['date'], sale_net, v['desc'][:50]))
    else:
        ratio = vat / sale_net
        if abs(ratio - Decimal('0.25')) < Decimal('0.01'):
            correct_25.append((v['ver'], sale_net, vat))
        else:
            weird.append((v['ver'], v['date'], sale_net, vat, ratio, v['desc'][:50]))

print(f'\nVERs with sales but NO VAT: {len(no_vat)}')
no_vat_total = sum(x[2] for x in no_vat)
print(f'  Total no-VAT sales in 3001/3051: {no_vat_total:.2f}')
for v in no_vat[:20]:
    print(f'  {v[0]} {v[1]} net={v[2]:>9.2f}  {v[3]}')

print(f'\nVERs with correct 25% VAT: {len(correct_25)}')
print(f'  Total: net={sum(x[1] for x in correct_25):.2f}, vat={sum(x[2] for x in correct_25):.2f}')

print(f'\nVERs with WEIRD VAT ratio: {len(weird)}')
for v in weird[:20]:
    print(f'  {v[0]} {v[1]} net={v[2]:>9.2f} vat={v[3]:>8.2f} ratio={v[4]:.4f} {v[5]}')

print()
print('=== BREAKDOWN BY BANK ===')
for bank, d in by_bank.items():
    expected_vat = d['net'] * Decimal('0.25')
    print(f'  {bank}: {d["count"]} sales, net={d["net"]:>10.2f}, vat={d["vat"]:>9.2f}, expected vat={expected_vat:>9.2f}, diff={d["vat"]-expected_vat:>+8.2f}')
