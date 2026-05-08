"""
Build VAT correction VER for Q1 2026.
- Reads MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
- For each expense booked GROSS that has Swedish 25% VAT, extracts the VAT
- Builds reverse-charge for foreign EU/non-EU digital services
- Outputs CORRECTIONS_INPUT_VAT_Q1_2026.se
"""
import re
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict

BASE = Path(r"c:\Users\samij\Desktop\Visma revesor info for old partner and new samisjackets and auronis vip\Q1_2026_PERIOD_2026-01_TO_2026-03")
SRC = BASE / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
OUT = BASE / "CORRECTIONS_INPUT_VAT_Q1_2026.se"

def D(x): return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# Read SE
text = SRC.read_text(encoding="cp437", errors="ignore")
ver_blocks = re.split(r'(?m)^#VER\s+', text)[1:]

vers = []
for part in ver_blocks:
    head = re.match(r'(\S+)\s+(\S+)\s+(\d{8})\s+"([^"]*)"', part)
    if not head: continue
    series, num, date, desc = head.groups()
    body = re.search(r'\{(.*?)\}\s*(?:\n|$)', part, re.DOTALL)
    if not body: continue
    trans = [(m.group(1), Decimal(m.group(2))) for m in
             re.finditer(r'#TRANS\s+(\d+)\s+\{[^}]*\}\s+(-?\d+\.?\d*)', body.group(1))]
    vers.append({"series": series, "num": num, "date": date, "desc": desc, "trans": trans})

# Index by num
by_num = {v["num"]: v for v in vers}

# === RULES ===
# Format: "VER_NUM": ("Reason", VAT_TO_RECLAIM, EXPENSE_ACCT_TO_REDUCE)
# When VAT_TO_RECLAIM is None, calculate as gross * 0.20 (= 25% of net)

SE_VAT_25 = [
    # VER, expense_acct (the one to reduce), reclaim_VAT_amount, note
    ("311",  "1460", D("625.00"),   "Unitrans freight - only 625 SEK domestic VAT (rest zero-rated intl)"),
    ("526",  "1460", D("2861.00"),  "Container Eskilstuna 14305 * 0.20"),
    ("271",  "5010", D("3125.40"),  "Lagar hyra 15627 * 0.20"),
    ("360",  "5010", D("1041.80"),  "Akvarium 5209 * 0.20"),
    # Fuel St1 / OKQ8 - 25% VAT
    ("275",  "5611", D("383.05"),   "OKQ8 1915.25 * 0.20"),
    ("103",  "5611", D("408.28"),   "St1 2041.40 * 0.20"),
    ("469",  "5611", D("420.04"),   "St1 2100.22 * 0.20"),
    ("404",  "5611", D("299.48"),   "St1 1497.42 * 0.20"),
    ("406",  "5611", D("299.48"),   "St1 1497.42 * 0.20"),
    ("400",  "5611", D("115.53"),   "St1 577.66 * 0.20"),
    ("402",  "5611", D("115.53"),   "St1 577.66 * 0.20"),
    # Parking Apcoa
    ("301",  "5611", D("79.05"),    "Apcoa 395.27 * 0.20"),
    ("92",   "5611", D("76.85"),    "Apcoa 384.27 * 0.20"),
    ("118",  "5611", D("112.00"),   "Parking 560.00 * 0.20"),
    # Telia/Tre mobile
    ("98",   "6212", D("113.80"),   "Mobil 569 * 0.20"),
    ("270",  "6212", D("113.80"),   "Mobil 569 * 0.20"),
    ("414",  "6212", D("113.80"),   "Mobil 569 * 0.20"),
    ("460",  "6212", D("213.73"),   "Tre 1068.64 * 0.20"),
    # Tradera / Amazon.se / Temu / Biltema (user confirmed to include)
    ("297",  "5410", D("1256.35"),  "Tradera 6281.74 * 0.20"),
    ("365",  "5410", D("415.33"),   "Temu 2076.65 * 0.20"),
    ("313",  "5410", D("321.16"),   "Amazon.se 1605.80 * 0.20"),
    ("315",  "5410", D("273.78"),   "Amazon 1368.92 * 0.20"),
    ("378",  "5410", D("185.61"),   "Tradera 928.06 * 0.20"),
    ("379",  "5410", D("185.50"),   "Tradera 927.50 * 0.20"),
    ("499",  "5410", D("143.42"),   "Tradera 717.10 * 0.20"),
    ("312",  "5410", D("114.51"),   "Tradera 572.55 * 0.20"),
    ("364",  "5410", D("88.44"),    "Temu 442.18 * 0.20"),
    ("189",  "5410", D("445.30"),   "Zalando 2226.48 * 0.20"),
    ("296",  "5460", D("224.98"),   "Biltema 1124.90 * 0.20"),
]

# EU/non-EU digital services SKIPPED per user request (no moms)
EU_SERVICES = []

# === Build VER bodies ===

# VER 998 - SE 25% VAT extractions
acct_changes_998 = defaultdict(Decimal)
for ver_num, exp_acct, vat, note in SE_VAT_25:
    if ver_num not in by_num:
        continue
    acct_changes_998[exp_acct] -= vat
    acct_changes_998["2641"] += vat

# VER 997 - skipped (user: IT services no moms)
acct_changes_997 = defaultdict(Decimal)

# === Write SE file ===

lines = []
lines.append("#FLAGGA 0")
lines.append('#PROGRAM "Manual VAT correction" "1.0"')
lines.append("#FORMAT PC8")
lines.append("#GEN 20260507")
lines.append("#SIETYP 4")
lines.append('#FNAMN "Samis Jackets AB"')
lines.append("#ORGNR 559489-5301")
lines.append("#KPTYP EUBAS97")
lines.append("#RAR 0 20260101 20261231")
lines.append("#RAR -1 20240701 20251231")
lines.append("")
lines.append('#KONTO 1460 "Lager av handelsvaror"')
lines.append('#KONTO 2641 "Debiterad ingaende moms"')
lines.append('#KONTO 5010 "Lokalhyra"')
lines.append('#KONTO 5410 "Forbrukningsinventarier"')
lines.append('#KONTO 5460 "Forbrukningsmaterial"')
lines.append('#KONTO 5611 "Drivmedel for personbilar"')
lines.append('#KONTO 6212 "Mobiltelefon"')
lines.append("")

# VER 998 - SE VAT extractions
lines.append('#VER A 998 20260331 "Q1 2026 input VAT extraction from gross-booked SE expenses"')
lines.append("{")
total_vat_998 = acct_changes_998["2641"]
lines.append(f"   #TRANS 2641 {{}} {total_vat_998:.2f}")
for acct in sorted(k for k in acct_changes_998 if k != "2641"):
    amt = acct_changes_998[acct]
    lines.append(f"   #TRANS {acct} {{}} {amt:.2f}")
lines.append("}")
lines.append("")

content = "\n".join(lines) + "\n"
OUT.write_text(content, encoding="utf-8")  # will be re-encoded after

# Print summary
print("=" * 70)
print("VER A 998 (SE VAT extractions) account changes:")
for acct, amt in sorted(acct_changes_998.items()):
    print(f"   {acct}: {amt:>12,.2f}")
print(f"   --- Sum: {sum(acct_changes_998.values()):,.2f} (must be 0)")
print()
print("VER A 997 (EU reverse charge) account changes:")
for acct, amt in sorted(acct_changes_997.items()):
    print(f"   {acct}: {amt:>12,.2f}")
print(f"   --- Sum: {sum(acct_changes_997.values()):,.2f} (must be 0)")
print()
print(f"Total Box 48 reclaim from VER 998: {acct_changes_998['2641']:,.2f} SEK")
print(f"Total Box 48 reclaim from VER 997: {acct_changes_997['2645']:,.2f} SEK")
print(f"Total Box 21 (EU services basis):  {acct_changes_997['4535']:,.2f} SEK")
print(f"Total Box 30 (output reverse VAT): {-acct_changes_997['2614']:,.2f} SEK")
print(f"\nFile written: {OUT}")
