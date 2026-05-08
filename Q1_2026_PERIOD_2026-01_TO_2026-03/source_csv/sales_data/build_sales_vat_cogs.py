"""SALES_AND_COGS_STANDALONE.se — ENDAST COGS (moms hanteras redan i bank-SE).

VIKTIGT — ARKITEKTUR (efter audit 2026-05-04):
  Bank-SE-filerna (LUNAR, WORLDLINE, WISE_EUR, MARGINALEN, WISE_USD) bokar
  REDAN sales NETTO + moms separat:
      Bank D brutto / 3001 K netto / 2611 K moms 20%
  → 2611 är KORREKT från bank-filerna. Ingen ny momsextraktion behövs.

  DENNA fil gör ENDAST COGS-bokningen för perioden:
      4010 D cogs / 1460 K cogs
  där cogs = 93 % × NETTO sales 25% (summan från bank-filerna).
"""
from __future__ import annotations
import re
from datetime import date
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "source_csv"
HERE = Path(__file__).resolve().parent
OUT = HERE / "SALES_AND_COGS_STANDALONE.se"
AUDIT = HERE / "SALES_VAT_COGS_FULL_AUDIT.md"

VER_RE = re.compile(r'^#VER\s+(\S+)\s+(\d+)\s+(\d{8})\s+"(.*?)"')
TRANS_RE = re.compile(r'^\s*#TRANS\s+(\d{4})\s+\{\}\s+(-?[\d.]+)')

VAT_SALES = {"3001", "3051"}
ZERO_SALES = {"3105", "3190"}
NON_SALES = {"3994"}
VAT_ACCT = "2611"
COGS_PCT = 0.93


def collect():
    by_month = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    vat_by_src = defaultdict(float)
    details = []
    for fp in sorted(SRC.rglob("*STANDALONE.se")):
        if fp.name.startswith("SALES_AND_COGS"):
            continue
        text = fp.read_text(encoding="cp437", errors="replace")
        cur = None
        for ln in text.splitlines():
            m = VER_RE.match(ln.strip())
            if m:
                cur = (m.group(3), m.group(1) + m.group(2))
                continue
            t = TRANS_RE.match(ln)
            if t and cur:
                konto, val = t.group(1), float(t.group(2))
                if konto in VAT_SALES or konto in ZERO_SALES or konto in NON_SALES:
                    netto = -val
                    ym = f"{cur[0][:4]}-{cur[0][4:6]}"
                    by_month[ym][konto][fp.name] += netto
                    details.append((cur[0], fp.name, cur[1], konto, netto))
                if konto == VAT_ACCT:
                    vat_by_src[fp.name] += val
    return by_month, details, vat_by_src


def build():
    by_month, details, vat_by_src = collect()
    today = date.today().strftime("%Y%m%d")
    L = []
    L.append("#FLAGGA 0")
    L.append('#PROGRAM "SamisJackets-COGS" "3.0"')
    L.append("#FORMAT PC8")
    L.append(f"#GEN {today}")
    L.append("#SIETYP 4")
    L.append('#FNAMN "Samis Jackets AB"')
    L.append("#ORGNR 559489-5301")
    L.append("#KPTYP EUBAS97")
    L.append("#RAR 0 20260101 20261231")
    L.append("#RAR -1 20240701 20251231")
    L.append('#KONTO 1460 "Lager av handelsvaror"')
    L.append('#KONTO 4110 "Kostnad sda varor"')
    L.append("#IB 0 1460 0.00")

    last_day = {"2026-01": "20260131", "2026-02": "20260228", "2026-03": "20260331"}
    ub = {"1460": 0.0, "4110": 0.0}
    ver_no = 1

    for ym in sorted(by_month):
        d = last_day.get(ym, ym.replace("-", "") + "01")
        netto_25 = 0.0
        for konto in sorted(VAT_SALES):
            netto_25 += round(sum(by_month[ym][konto].values()), 2)
        if netto_25 > 0:
            cogs = round(netto_25 * COGS_PCT, 2)
            L.append(f'#VER C {ver_no} {d} "KSV {ym} 93pct av netto-25-sales {netto_25:.2f}"')
            L.append("{")
            L.append(f"   #TRANS 4110 {{}} {cogs:.2f}")
            L.append(f"   #TRANS 1460 {{}} {-cogs:.2f}")
            L.append("}")
            ub["4110"] += cogs
            ub["1460"] += -cogs
            ver_no += 1

    # MANUELL COGS for Norge grosshandel (3 fakturor i feb, totalt 58 000 sales 0%)
    # Inkopskostnad var 80 000 -> forlustaffar -22 000.
    norge_cogs = 80000.00
    L.append(f'#VER C {ver_no} 20260228 "KSV Norge grosshandel feb 2026 (sales 58000, kostnad 80000 -> forlust 22000)"')
    L.append("{")
    L.append(f"   #TRANS 4110 {{}} {norge_cogs:.2f}")
    L.append(f"   #TRANS 1460 {{}} {-norge_cogs:.2f}")
    L.append("}")
    ub["4110"] += norge_cogs
    ub["1460"] += -norge_cogs
    ver_no += 1

    L.append(f'#UB 0 1460 {ub["1460"]:.2f}')
    L.append(f'#RES 0 4110 {ub["4110"]:.2f}')

    OUT.write_bytes(("\r\n".join(L) + "\r\n").encode("cp437", errors="replace"))
    return by_month, details, vat_by_src, ub


def write_audit(by_month, details, vat_by_src, ub):
    A = []
    A.append("# SALES + VAT + COGS — FULL AUDIT Q1 2026 (v3 — moms-dubblering fixad)")
    A.append("")
    A.append("## Arkitektur (KORREKT)")
    A.append("")
    A.append("Bank-SE-filerna bokar sales NETTO + moms separat:")
    A.append("")
    A.append("```")
    A.append("Bank  D brutto")
    A.append("3001  K netto (80 % av brutto)")
    A.append("2611  K moms  (20 % av brutto)")
    A.append("```")
    A.append("")
    A.append("→ `2611` är **redan korrekt** efter bank-import. Ingen ytterligare momsextraktion sker.")
    A.append("→ Denna fil bokar **enbart COGS**: `4010 D / 1460 K` = 93 % × netto-25%-sales per månad.")
    A.append("")
    A.append("## Moms 2611 per källfil (redan bokat av bank-SE)")
    A.append("")
    A.append("| Källa | 2611-summa (kredit−) |")
    A.append("|---|--:|")
    g_vat = 0.0
    for src in sorted(vat_by_src):
        v = vat_by_src[src]
        if abs(v) < 0.01: continue
        g_vat += v
        A.append(f"| {src} | {v:>14,.2f} |")
    A.append(f"| **Σ utgående moms 2611** | **{g_vat:>14,.2f}** |")
    A.append(f"| **Att betala till SKV (positiv = skuld)** | **{-g_vat:>14,.2f}** |")
    A.append("")
    A.append("## Sales NETTO per månad/konto/källa")
    A.append("")
    A.append("| Månad | Konto | Källa | Netto SEK |")
    A.append("|---|---|---|--:|")
    for ym in sorted(by_month):
        for k in sorted(by_month[ym]):
            for src, v in sorted(by_month[ym][k].items()):
                A.append(f"| {ym} | {k} | {src} | {v:>12,.2f} |")
    A.append("")
    A.append("## COGS-kalkyl")
    A.append("")
    A.append("| Månad | Netto 25% sales | COGS 93% |")
    A.append("|---|--:|--:|")
    g_net = g_cogs = 0.0
    for ym in sorted(by_month):
        netto_25 = sum(round(sum(by_month[ym][k].values()), 2) for k in VAT_SALES)
        if netto_25 <= 0:
            continue
        cogs = round(netto_25 * COGS_PCT, 2)
        g_net += netto_25
        g_cogs += cogs
        A.append(f"| {ym} | {netto_25:,.2f} | {cogs:,.2f} |")
    A.append(f"| **Σ** | **{g_net:,.2f}** | **{g_cogs:,.2f}** |")
    A.append("")
    A.append("## Slutsiffror Q1 2026")
    A.append("")
    g_zero = sum(b for _, _, _, k, b in details if k in ZERO_SALES)
    g_ins = sum(b for _, _, _, k, b in details if k in NON_SALES)
    A.append("| Post | SEK |")
    A.append("|---|--:|")
    A.append(f"| Netto sales 25 % (3001+3051) | {g_net:,.2f} |")
    A.append(f"| Sales 0 % utland (3105+3190) | {g_zero:,.2f} |")
    A.append(f"| Försäkringsersättning (3994 — separat) | {g_ins:,.2f} |")
    A.append(f"| **Total intäkter (sales+försäkring)** | **{g_net + g_zero + g_ins:,.2f}** |")
    A.append(f"| Utgående moms 2611 (skuld till SKV) | {-g_vat:,.2f} |")
    A.append(f"| KSV 4110 (93 % × netto-25%) | {ub['4110']:,.2f} |")
    A.append(f"| Bruttomarginal (netto-25% − KSV) | {g_net - ub['4110']:,.2f} |")
    A.append("")
    AUDIT.write_text("\n".join(A) + "\n", encoding="utf-8")


def main():
    by_month, details, vat_by_src, ub = build()
    write_audit(by_month, details, vat_by_src, ub)
    print(f"OK -> {OUT.relative_to(ROOT)}")
    print(f"OK -> {AUDIT.relative_to(ROOT)}")
    g_net = sum(b for _, _, _, k, b in details if k in VAT_SALES)
    g_zero = sum(b for _, _, _, k, b in details if k in ZERO_SALES)
    g_ins = sum(b for _, _, _, k, b in details if k in NON_SALES)
    g_vat = sum(vat_by_src.values())
    print(f"Netto sales 25%:        {g_net:>14,.2f}")
    print(f"Sales 0% utland:        {g_zero:>14,.2f}")
    print(f"Forsakring 3994:        {g_ins:>14,.2f}")
    print(f"Moms 2611 (bank):       {g_vat:>14,.2f}  (skuld SKV: {-g_vat:,.2f})")
    print(f"KSV 4110:               {ub['4110']:>14,.2f}")


if __name__ == "__main__":
    main()
