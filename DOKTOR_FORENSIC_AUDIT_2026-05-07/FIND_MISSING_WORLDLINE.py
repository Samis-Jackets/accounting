"""Find which Marginalen B-transactions are missing as Worldline sales in master."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from FAST_SALES_AUDIT import parse_se_file, MARGINALEN_SRC, MASTER, get_bank_amount, is_sales_ver, get_sales_amounts
from decimal import Decimal

marg_vers = parse_se_file(MARGINALEN_SRC)
master_vers = parse_se_file(MASTER)

# Source: B-transactions (Worldline deposits to Marginalen)
src_b = []
for v in marg_vers:
    if v['desc'].startswith('B') and len(v['desc']) > 1 and v['desc'][1].isdigit():
        amt = get_bank_amount(v, '1930')
        src_b.append((v['date'], v['desc'], amt))

# Master: Worldline sales (debit 1947 with credit to 3001/3051)
master_wl = []
for v in master_vers:
    if not is_sales_ver(v):
        continue
    bank_used = None
    for acc, amt in v['trans']:
        if amt > 0 and acc in ('1930', '1944', '1947', '1948', '1910'):
            bank_used = acc
            break
    if bank_used == '1947':
        net, vat, gross = get_sales_amounts(v)
        master_wl.append((v['date'], v['desc'], gross))

print(f"Marginalen B-trans: {len(src_b)} = {sum(a for _,_,a in src_b):.2f}")
print(f"Master Worldline:   {len(master_wl)} = {sum(a for _,_,a in master_wl):.2f}")
print(f"Diff: {sum(a for _,_,a in src_b) - sum(a for _,_,a in master_wl):.2f}")

# Match by amount (B-trans amount = Worldline gross sales)
master_amounts = sorted([(d, g) for d, _, g in master_wl])
src_amounts = sorted([(d, g) for d, _, g in src_b])

# Pair them up - find unmatched
master_remaining = list(master_amounts)
unmatched_src = []
for sd, sg in src_amounts:
    found = False
    for i, (md, mg) in enumerate(master_remaining):
        if abs(sg - mg) < Decimal('0.50'):
            master_remaining.pop(i)
            found = True
            break
    if not found:
        unmatched_src.append((sd, sg))

print(f"\n=== UNMATCHED B-trans in Marginalen (NOT in master as Worldline sales) ===")
for d, g in unmatched_src:
    # Find original B-trans desc
    for sd, sdesc, sg in src_b:
        if sd == d and sg == g:
            print(f"  {d}  {sdesc:<25}  {g:>12.2f}")
            break

print(f"\n=== UNMATCHED master Worldline sales (NOT in Marginalen B-trans) ===")
for d, g in master_remaining:
    print(f"  {d}  {g:>12.2f}")

print(f"\nTotal unmatched src: {sum(g for _,g in unmatched_src):.2f}")
print(f"Total unmatched master: {sum(g for _,g in master_remaining):.2f}")
