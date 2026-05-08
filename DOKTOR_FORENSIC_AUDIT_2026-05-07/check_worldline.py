import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file, is_sales_ver, get_sales_amounts
from pathlib import Path
from decimal import Decimal

p = Path(r'c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03\source_csv\worldline\WORLDLINE_STANDALONE.se')
vers = parse_se_file(p)
print('Total VERs:', len(vers))
sales = [v for v in vers if is_sales_ver(v)]
print('Sales VERs:', len(sales))
total_net = Decimal('0')
total_vat = Decimal('0')
for v in sales:
    n, vt, g = get_sales_amounts(v)
    total_net += n
    total_vat += vt
print(f'Worldline source: net={total_net:.2f}, vat={total_vat:.2f}, gross={total_net+total_vat:.2f}')
non_sales = [v for v in vers if not is_sales_ver(v)]
print(f'Non-sales VERs: {len(non_sales)}')
for v in non_sales[:5]:
    print(' ', v['ver'], v['date'], v['desc'][:50], '->', v['trans'])
