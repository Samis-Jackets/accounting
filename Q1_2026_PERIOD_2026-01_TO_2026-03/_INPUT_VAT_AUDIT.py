"""
INPUT VAT (Ingaende moms / Box 48) AUDIT
Scans master SE + Doktor Visma SE for Q1 2026.
- Reports current input VAT (264x credits)
- Finds expense entries WITHOUT VAT extraction that likely should have VAT
"""
import re
from pathlib import Path
from collections import defaultdict
from decimal import Decimal

BASE = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")

FILES = [
    BASE / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se",
    BASE / "Doktor invistgthion skattverket" / "20260101-20261231 (1).se",
]

# Swedish VAT-bearing expense accounts - if these have entries WITHOUT a 264x in same VER, VAT may be missing
VAT_BEARING_EXPENSE = {
    # 5xxx costs
    "5010","5011","5020","5060","5090","5410","5420","5430","5440","5450","5460","5470","5480","5490",
    "5500","5510","5520","5530","5540","5550","5560","5610","5611","5612","5613","5615","5616","5620",
    "5800","5810","5820","5830","5832","5840","5890","5900","5910","5920","5930","5940","5950","5960","5990",
    "6071","6072","6090","6110","6150","6212","6230","6250","6310","6420","6470","6530","6540","6550","6560","6570","6590",
    "6970","6980","6981","6982","6991","6992","6993","6999",
    "7610","7621","7631",
    # asset purchases
    "1220","1221","1222","1230","1240","1250","1260","1290",
    "1460","1465","1469",
}
INPUT_VAT_ACCT = {"2640","2641","2642","2645","2646","2647","2648"}
OUTPUT_VAT_ACCT = {"2610","2611","2612","2614","2615","2620","2621","2630","2631","2640"}  # exclude 2640 from output
IMPORT_BASIS = {"4515","4516","4517","4518","4531","4532","4535","4536","4537","4545","4546","4547"}

VER_RE = re.compile(r'^#VER\s+(\S+)\s+(\S+)\s+(\d{8})\s+"([^"]*)"', re.MULTILINE)
TRANS_RE = re.compile(r'^#TRANS\s+(\d+)\s+\{[^}]*\}\s+(-?\d+\.?\d*)', re.MULTILINE)

def parse(path):
    text = path.read_text(encoding="cp437", errors="ignore")
    vers = []
    # split on #VER
    parts = re.split(r'(?m)^#VER\s+', text)
    for part in parts[1:]:
        head_match = re.match(r'(\S+)\s+(\S+)\s+(\d{8})\s+"([^"]*)"', part)
        if not head_match:
            continue
        series, num, date, desc = head_match.groups()
        # find lines between { and }
        m = re.search(r'\{(.*?)\}\s*(?:\n|$)', part, re.DOTALL)
        if not m:
            continue
        body = m.group(1)
        trans = []
        for tm in re.finditer(r'#TRANS\s+(\d+)\s+\{[^}]*\}\s+(-?\d+\.?\d*)', body):
            trans.append((tm.group(1), Decimal(tm.group(2))))
        vers.append({"series": series, "num": num, "date": date, "desc": desc, "trans": trans})
    return vers

def audit_file(path):
    print(f"\n{'='*80}\nFILE: {path.name}\n{'='*80}")
    if not path.exists():
        print("NOT FOUND"); return
    vers = parse(path)
    print(f"VERs parsed: {len(vers)}")

    # Q1 only
    q1 = [v for v in vers if v["date"].startswith("202601") or v["date"].startswith("202602") or v["date"].startswith("202603")]
    print(f"Q1 2026 VERs: {len(q1)}")

    # Account totals (Q1)
    acct_totals = defaultdict(Decimal)
    for v in q1:
        for a, amt in v["trans"]:
            acct_totals[a] += amt

    print("\n--- VAT account balances Q1 2026 ---")
    for a in sorted(set(list(INPUT_VAT_ACCT) + list(OUTPUT_VAT_ACCT) + list(IMPORT_BASIS))):
        if a in acct_totals:
            print(f"  {a}: {acct_totals[a]:>15,.2f}")

    # Find Q1 expense entries WITHOUT input VAT in same VER
    print("\n--- Q1 expense VERs MISSING input VAT (potential reclaim) ---")
    missing = []
    for v in q1:
        accts_in_ver = {a for a, _ in v["trans"]}
        has_input_vat = bool(accts_in_ver & INPUT_VAT_ACCT)
        has_import_basis = bool(accts_in_ver & IMPORT_BASIS)
        if has_input_vat or has_import_basis:
            continue
        # find vat-bearing expense lines (debit only)
        expense_amount = Decimal("0")
        expense_accts = []
        for a, amt in v["trans"]:
            if a in VAT_BEARING_EXPENSE and amt > 0:
                expense_amount += amt
                expense_accts.append((a, amt))
        if expense_amount > 100:  # ignore tiny
            missing.append((v, expense_amount, expense_accts))

    missing.sort(key=lambda x: -x[1])
    total_missed_basis = Decimal("0")
    for v, amt, accts in missing[:50]:
        potential_vat = amt * Decimal("0.20")  # 25% of 80% gross = 20% of total if booked gross
        # but expense booked NET means VAT to reclaim = amt * 0.25
        # We don't know if booked gross or net - assume gross (VAT-inclusive) -> reclaim = amt*0.20
        # If booked net -> reclaim = amt*0.25
        total_missed_basis += amt
        accts_str = ", ".join(f"{a}={x:,.0f}" for a, x in accts[:3])
        print(f"  {v['series']} {v['num']:>4} {v['date']} | {amt:>12,.2f} | {accts_str} | {v['desc'][:50]}")

    print(f"\nTotal expense lines missing VAT: {total_missed_basis:,.2f}")
    print(f"  If booked GROSS (VAT included): potential reclaim ~ {total_missed_basis * Decimal('0.20'):,.2f}")
    print(f"  If booked NET (VAT excluded):    potential reclaim ~ {total_missed_basis * Decimal('0.25'):,.2f}")
    return missing

for f in FILES:
    audit_file(f)
