"""
FAST SALES AUDIT - Q1 2026
Cross-check sales between source files (Marginalen, Lunar, Wise EUR)
and verify they all appear in the master SE file.

Sources:
- Marginalen: ONLY "B..." transactions (Worldline card deposits) = sales
- Lunar (1948): customer payments to bank = sales (excluding insurance/bidrag)
- Wise EUR (1944): Stripe EUR payments = sales

Master file: MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
"""
import re
from pathlib import Path
from decimal import Decimal
from collections import defaultdict

BASE = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
MASTER = BASE / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
MARGINALEN_SRC = BASE / "source_csv" / "marginalen" / "MARGINALEN_STANDALONE.se"
LUNAR_SRC = BASE / "source_csv" / "Lunar Bank" / "LUNAR_STANDALONE.se"
WISE_EUR_SRC = BASE / "source_csv" / "wise" / "eur" / "WISE_EUR_STANDALONE.se"

OUT_REPORT = Path(__file__).parent / "FAST_SALES_AUDIT_REPORT.txt"


def parse_se_file(path):
    """Return list of {ver, series, ver_num, date, desc, transactions[(account, amount)]}"""
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        # Skip blank lines (some standalone files have double-spacing)
        lines = [l for l in f.readlines() if l.strip()]
    
    vers = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'#VER\s+(\w+)\s+(\d+)\s+(\d{8})\s+"([^"]*)"', line)
        if m:
            series, ver_num, date, desc = m.groups()
            i += 1
            trans = []
            if i < len(lines) and '{' in lines[i]:
                i += 1
                while i < len(lines) and lines[i].strip() != '}':
                    tm = re.match(r'\s*#TRANS\s+(\d+)\s+\{\}\s+(-?[\d.]+)', lines[i])
                    if tm:
                        trans.append((tm.group(1), Decimal(tm.group(2))))
                    i += 1
            vers.append({
                'ver': f"{series} {ver_num}",
                'series': series,
                'ver_num': ver_num,
                'date': date,
                'desc': desc,
                'trans': trans
            })
        i += 1
    return vers


def is_sales_ver(ver):
    """A VER is a sale if it credits 3001/3051/3105/3190 (sales accounts)."""
    sales_accounts = {'3001', '3051', '3105', '3190'}
    for acc, amt in ver['trans']:
        if acc in sales_accounts and amt < 0:
            return True
    return False


def get_sales_amounts(ver):
    """Returns (net_sales, vat, gross) for the VER."""
    net = Decimal('0')
    vat = Decimal('0')
    sales_accounts = {'3001', '3051', '3105', '3190'}
    vat_accounts = {'2611'}
    for acc, amt in ver['trans']:
        if acc in sales_accounts:
            net += -amt  # credits are negative
        elif acc in vat_accounts:
            vat += -amt
    return net, vat, net + vat


def get_bank_amount(ver, bank_acc):
    """Get debit amount to bank account."""
    for acc, amt in ver['trans']:
        if acc == bank_acc and amt > 0:
            return amt
    return Decimal('0')


def main():
    out = []
    def w(s=''):
        out.append(s)
        print(s)
    
    w("=" * 100)
    w("FAST SALES AUDIT - Q1 2026 - Samis Jackets AB (559489-5301)")
    w("Sources: Marginalen (B-trans only), Lunar (1948), Wise EUR (1944)")
    w("Target:  MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    w("=" * 100)
    
    # ---- Parse all files ----
    master_vers = parse_se_file(MASTER)
    marg_vers = parse_se_file(MARGINALEN_SRC)
    lunar_vers = parse_se_file(LUNAR_SRC)
    wise_vers = parse_se_file(WISE_EUR_SRC)
    
    w(f"\nMaster VERs:     {len(master_vers)}")
    w(f"Marginalen VERs: {len(marg_vers)}")
    w(f"Lunar VERs:      {len(lunar_vers)}")
    w(f"Wise EUR VERs:   {len(wise_vers)}")
    
    # ============================================================
    # 1. MARGINALEN SALES (only "B..." transactions = Worldline)
    # ============================================================
    w("\n" + "=" * 100)
    w("[1] MARGINALEN SOURCE -> Worldline card sales (descriptions starting with 'B')")
    w("=" * 100)
    
    # In source file: VER for Worldline shows: debit 1930, credit 1947 (transfer)
    # In master file: should appear as actual sales (debit 1930, credit 3001/3051, credit 2611)
    # OR as transfer 1930<-1947 with separate sales VER from worldline source
    # Per user: ONLY count Marginalen B-transactions as Worldline sales source-of-truth
    
    marg_b_trans = [v for v in marg_vers if v['desc'].startswith('B') and len(v['desc']) > 1 and v['desc'][1].isdigit()]
    marg_b_total = Decimal('0')
    w(f"\nFound {len(marg_b_trans)} 'B...' transactions in Marginalen source")
    w(f"{'Date':<10} {'Desc':<25} {'Amount':>12}")
    w("-" * 60)
    for v in marg_b_trans:
        amt = get_bank_amount(v, '1930')
        marg_b_total += amt
        w(f"{v['date']:<10} {v['desc'][:24]:<25} {amt:>12.2f}")
    w("-" * 60)
    w(f"{'TOTAL Worldline sales (Marginalen B-trans)':<36} {marg_b_total:>12.2f} SEK")
    
    # ============================================================
    # 2. LUNAR SALES (account 1948)
    # ============================================================
    w("\n" + "=" * 100)
    w("[2] LUNAR SOURCE -> Customer payments (excl insurance/bidrag)")
    w("=" * 100)
    
    lunar_sales = []
    lunar_other = []
    for v in lunar_vers:
        # Check what's credited
        is_insurance_or_bidrag = any(acc in ('3994', '3985') for acc, _ in v['trans'])
        if is_insurance_or_bidrag:
            lunar_other.append(v)
        elif is_sales_ver(v):
            lunar_sales.append(v)
        else:
            # Check if it's a customer deposit (debit 1948 with no expense account)
            bank_in = get_bank_amount(v, '1948')
            if bank_in > 0:
                lunar_other.append(v)
    
    lunar_total_net = Decimal('0')
    lunar_total_vat = Decimal('0')
    lunar_total_gross = Decimal('0')
    w(f"\n{'VER':<8} {'Date':<10} {'Desc':<35} {'Net':>10} {'VAT':>10} {'Gross':>10}")
    w("-" * 90)
    for v in lunar_sales:
        net, vat, gross = get_sales_amounts(v)
        lunar_total_net += net
        lunar_total_vat += vat
        lunar_total_gross += gross
        w(f"{v['ver']:<8} {v['date']:<10} {v['desc'][:34]:<35} {net:>10.2f} {vat:>10.2f} {gross:>10.2f}")
    w("-" * 90)
    w(f"{'TOTAL LUNAR SALES':<54} {lunar_total_net:>10.2f} {lunar_total_vat:>10.2f} {lunar_total_gross:>10.2f}")
    
    if lunar_other:
        w(f"\nLunar non-sales income (insurance 3994 / bidrag 3985 / other):")
        for v in lunar_other:
            for acc, amt in v['trans']:
                if acc in ('3994', '3985'):
                    w(f"  {v['ver']:<8} {v['date']:<10} {v['desc'][:50]:<50} acc {acc}: {-amt:>10.2f}")
    
    # ============================================================
    # 3. WISE EUR SALES (account 1944)
    # ============================================================
    w("\n" + "=" * 100)
    w("[3] WISE EUR SOURCE -> Stripe EUR sales")
    w("=" * 100)
    
    wise_sales = [v for v in wise_vers if is_sales_ver(v)]
    wise_total_net = Decimal('0')
    wise_total_vat = Decimal('0')
    wise_total_gross = Decimal('0')
    w(f"\nFound {len(wise_sales)} sales VERs in Wise EUR source")
    w(f"{'VER':<8} {'Date':<10} {'Desc':<35} {'Net':>10} {'VAT':>10} {'Gross':>10}")
    w("-" * 90)
    for v in wise_sales:
        net, vat, gross = get_sales_amounts(v)
        wise_total_net += net
        wise_total_vat += vat
        wise_total_gross += gross
        w(f"{v['ver']:<8} {v['date']:<10} {v['desc'][:34]:<35} {net:>10.2f} {vat:>10.2f} {gross:>10.2f}")
    w("-" * 90)
    w(f"{'TOTAL WISE EUR SALES':<54} {wise_total_net:>10.2f} {wise_total_vat:>10.2f} {wise_total_gross:>10.2f}")
    
    # ============================================================
    # 4. CROSS-CHECK MASTER FILE
    # ============================================================
    w("\n" + "=" * 100)
    w("[4] MASTER FILE - All sales recorded (by sales account)")
    w("=" * 100)
    
    # Collect all sales credits from master, grouped by which bank account is debited
    master_sales_by_bank = defaultdict(lambda: {'net': Decimal('0'), 'vat': Decimal('0'), 'count': 0, 'vers': []})
    master_total_net = Decimal('0')
    master_total_vat = Decimal('0')
    
    for v in master_vers:
        if not is_sales_ver(v):
            continue
        net, vat, gross = get_sales_amounts(v)
        master_total_net += net
        master_total_vat += vat
        # Find which bank account is debited
        bank_used = 'OTHER'
        for acc, amt in v['trans']:
            if amt > 0 and acc in ('1930', '1944', '1947', '1948', '1910'):
                bank_used = acc
                break
        master_sales_by_bank[bank_used]['net'] += net
        master_sales_by_bank[bank_used]['vat'] += vat
        master_sales_by_bank[bank_used]['count'] += 1
        master_sales_by_bank[bank_used]['vers'].append(v)
    
    bank_names = {
        '1930': 'Marginalen (direct)',
        '1944': 'Wise EUR (Stripe)',
        '1947': 'Worldline (card)',
        '1948': 'Lunar Bank',
        '1910': 'Cash (Kassa)',
        'OTHER': 'Other/journal'
    }
    
    w(f"\n{'Bank Acc':<10} {'Name':<25} {'#':>4} {'Net':>12} {'VAT':>12} {'Gross':>12}")
    w("-" * 80)
    for acc in ['1930', '1944', '1947', '1948', '1910', 'OTHER']:
        d = master_sales_by_bank[acc]
        if d['count'] > 0:
            w(f"{acc:<10} {bank_names[acc]:<25} {d['count']:>4} {d['net']:>12.2f} {d['vat']:>12.2f} {(d['net']+d['vat']):>12.2f}")
    w("-" * 80)
    w(f"{'TOTAL MASTER SALES':<41} {master_total_net:>12.2f} {master_total_vat:>12.2f} {(master_total_net+master_total_vat):>12.2f}")
    
    # ============================================================
    # 5. RECONCILIATION
    # ============================================================
    w("\n" + "=" * 100)
    w("[5] RECONCILIATION - Source vs Master")
    w("=" * 100)
    
    # Worldline source = Marginalen B-trans
    worldline_master = master_sales_by_bank['1947']['net'] + master_sales_by_bank['1947']['vat']
    # Plus any direct 1930 sales attributed to worldline... 
    # User's rule: Marginalen B-trans = Worldline sales source of truth
    # In master, Worldline sales appear as debit 1947 (when card processed) credit 3001/2611
    # And then transfer 1930 <- 1947 (the B transactions)
    
    w(f"\nWORLDLINE/MARGINALEN B-trans:")
    w(f"  Source (Marginalen B-trans bank-in): {marg_b_total:>12.2f} SEK gross")
    w(f"  Master sales via 1947 (Worldline) :  {worldline_master:>12.2f} SEK gross")
    diff_w = marg_b_total - worldline_master
    status_w = 'OK' if abs(diff_w) < Decimal('1') else 'MISMATCH'
    w(f"  Diff: {diff_w:>12.2f}  [{status_w}]")
    
    lunar_master_gross = master_sales_by_bank['1948']['net'] + master_sales_by_bank['1948']['vat']
    w(f"\nLUNAR:")
    w(f"  Source sales gross:  {lunar_total_gross:>12.2f} SEK")
    w(f"  Master 1948 sales :  {lunar_master_gross:>12.2f} SEK")
    diff_l = lunar_total_gross - lunar_master_gross
    status_l = 'OK' if abs(diff_l) < Decimal('1') else 'MISMATCH'
    w(f"  Diff: {diff_l:>12.2f}  [{status_l}]")
    
    wise_master_gross = master_sales_by_bank['1944']['net'] + master_sales_by_bank['1944']['vat']
    w(f"\nWISE EUR (Stripe):")
    w(f"  Source sales gross:  {wise_total_gross:>12.2f} SEK")
    w(f"  Master 1944 sales :  {wise_master_gross:>12.2f} SEK")
    diff_we = wise_total_gross - wise_master_gross
    status_we = 'OK' if abs(diff_we) < Decimal('1') else 'MISMATCH'
    w(f"  Diff: {diff_we:>12.2f}  [{status_we}]")
    
    # ============================================================
    # 6. GRAND TOTAL
    # ============================================================
    w("\n" + "=" * 100)
    w("[6] GRAND TOTAL Q1 2026 SALES")
    w("=" * 100)
    
    source_total = marg_b_total + lunar_total_gross + wise_total_gross
    master_total_gross = master_total_net + master_total_vat
    
    w(f"\nSOURCE TOTAL (Marginalen B + Lunar + Wise EUR):  {source_total:>12.2f} SEK gross")
    w(f"MASTER TOTAL (all sales 3001/3051/3105/3190):    {master_total_gross:>12.2f} SEK gross")
    w(f"  - Net:  {master_total_net:>12.2f} SEK")
    w(f"  - VAT:  {master_total_vat:>12.2f} SEK")
    w(f"DIFF:                                             {(master_total_gross - source_total):>12.2f} SEK")
    w(f"  (positive = master has more than 3 sources => includes cash sales / direct Marginalen)")
    
    # Cash sales 1910
    cash_gross = master_sales_by_bank['1910']['net'] + master_sales_by_bank['1910']['vat']
    direct_marg = master_sales_by_bank['1930']['net'] + master_sales_by_bank['1930']['vat']
    other = master_sales_by_bank['OTHER']['net'] + master_sales_by_bank['OTHER']['vat']
    w(f"\nReconciling extras in master:")
    w(f"  Cash sales (1910):           {cash_gross:>12.2f} SEK")
    w(f"  Direct Marginalen (1930):    {direct_marg:>12.2f} SEK")
    w(f"  Other/journal:               {other:>12.2f} SEK")
    w(f"  Sum: {(cash_gross + direct_marg + other):>12.2f} SEK")
    
    expected_master = source_total + cash_gross + direct_marg + other
    final_diff = master_total_gross - expected_master
    w(f"\nExpected master = sources + cash + direct + other = {expected_master:>12.2f} SEK")
    w(f"Actual master                                       = {master_total_gross:>12.2f} SEK")
    w(f"FINAL DIFF                                          = {final_diff:>12.2f} SEK")
    
    if abs(final_diff) < Decimal('1'):
        w("\n[STATUS] OK - All sales reconcile correctly. NO MISSING SALES.")
    else:
        w(f"\n[STATUS] DISCREPANCY of {final_diff:.2f} SEK detected - needs investigation.")
    
    w("\n" + "=" * 100)
    w("AUDIT COMPLETE")
    w("=" * 100)
    
    OUT_REPORT.write_text("\n".join(out), encoding='utf-8')
    print(f"\nReport saved to: {OUT_REPORT}")


if __name__ == '__main__':
    main()
