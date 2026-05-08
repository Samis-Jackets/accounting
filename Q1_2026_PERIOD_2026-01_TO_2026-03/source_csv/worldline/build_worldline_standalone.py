"""Bygg WORLDLINE_STANDALONE.se från PROPOSED_worldline_Q1_2026.se.

PROPOSED-filen har 3051 utan momssplit. Här delar vi 80/20:
  - 1947 D = gross
  - 3051 K = 80% (netto sales ex moms)
  - 2611 K = 20% (utgående moms 25%)

Bank-fees lämnas oförändrade (1947 K / 6570 D).
"""
from __future__ import annotations
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "PROPOSED_worldline_Q1_2026.se"
OUT = ROOT / "WORLDLINE_STANDALONE.se"

VER_RE = re.compile(r'^#VER\s+(\S+)\s+(\d+)\s+(\d{8})\s+"(.*)"')
TRANS_RE = re.compile(r"^\s*#TRANS\s+(\d{4})\s+\{\}\s+(-?[\d.]+)")


def parse_proposed():
    text = SRC.read_text(encoding="cp437", errors="replace")
    blocks = []
    cur = None
    for line in text.split("\n"):
        line = line.rstrip("\r")
        m = VER_RE.match(line)
        if m:
            if cur:
                blocks.append(cur)
            cur = {"ver": m.group(2), "date": m.group(3), "desc": m.group(4), "trans": []}
            continue
        t = TRANS_RE.match(line)
        if t and cur is not None:
            cur["trans"].append((t.group(1), float(t.group(2))))
    if cur:
        blocks.append(cur)
    return blocks


def build():
    blocks = parse_proposed()
    today = date.today().strftime("%Y%m%d")
    out = []
    out.append("#FLAGGA 0")
    out.append('#PROGRAM "SamisJackets-Worldline" "1.0"')
    out.append("#FORMAT PC8")
    out.append(f"#GEN {today}")
    out.append("#SIETYP 4")
    out.append('#FNAMN "Samis Jackets AB"')
    out.append("#ORGNR 559489-5301")
    out.append("#KPTYP EUBAS97")
    out.append("#RAR 0 20260101 20261231")
    out.append("#RAR -1 20240701 20251231")
    out.append('#KONTO 1947 "Worldline kortinlösen-konto"')
    out.append('#KONTO 2611 "Utgående moms 25%"')
    out.append('#KONTO 3051 "Försäljning Shopify/Swish 25% moms"')
    out.append('#KONTO 6570 "Bankkostnader"')
    out.append("#IB 0 1947 0.00")

    totals = {"1947": 0.0, "2611": 0.0, "3051": 0.0, "6570": 0.0}
    ver_no = 0
    for b in blocks:
        ver_no += 1
        # Identify SALES vs FEE
        is_sales = any(t[0] == "3051" for t in b["trans"])
        if is_sales:
            # 1947 D gross, 3051 -gross  -> split 3051 K 80% + 2611 K 20%
            gross = next(amt for k, amt in b["trans"] if k == "1947")
            moms = round(gross * 0.20, 2)
            netto = round(gross - moms, 2)
            out.append(f'#VER W {ver_no} {b["date"]} "{b["desc"]}"')
            out.append("{")
            out.append(f"   #TRANS 1947 {{}} {gross:.2f}")
            out.append(f"   #TRANS 3051 {{}} {-netto:.2f}")
            out.append(f"   #TRANS 2611 {{}} {-moms:.2f}")
            out.append("}")
            totals["1947"] += gross
            totals["3051"] += -netto
            totals["2611"] += -moms
        else:
            # FEE: 1947 -fee / 6570 +fee
            out.append(f'#VER W {ver_no} {b["date"]} "{b["desc"]}"')
            out.append("{")
            for k, amt in b["trans"]:
                out.append(f"   #TRANS {k} {{}} {amt:.2f}")
                totals[k] += amt
            out.append("}")

    out.append(f'#UB 0 1947 {round(totals["1947"], 2):.2f}')
    out.append(f'#UB 0 2611 {round(totals["2611"], 2):.2f}')
    out.append(f'#RES 0 3051 {round(totals["3051"], 2):.2f}')
    out.append(f'#RES 0 6570 {round(totals["6570"], 2):.2f}')

    OUT.write_text("\r\n".join(out) + "\r\n", encoding="cp437", errors="replace")
    print(f"OK -> {OUT}")
    print(f"VER: {ver_no}")
    print(f"Totals: 1947={totals['1947']:,.2f}  3051={totals['3051']:,.2f}  2611={totals['2611']:,.2f}  6570={totals['6570']:,.2f}")


if __name__ == "__main__":
    build()
