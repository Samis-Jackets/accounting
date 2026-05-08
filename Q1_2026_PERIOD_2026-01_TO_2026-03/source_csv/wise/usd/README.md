# Wise USD – snabbreferens

Bankkonto i BAS: **1942**  Valuta: **USD**  Kvartalsrate Q1 2026: **9,40 SEK/USD**

## Huvudreferens
- `..\..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik B2C 25 %
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `METHODOLOGY_USD.md` (utfört exempel med beslut)

## Försäljning B2C 25 % (Future World Tech / Marketplace USD)
Inkommande USD-payouts från marketplace bokas:
- **1942** debet (brutto, omräknat till SEK med 9,40)
- **3051** kredit (netto = brutto/1.25)
- **2611** kredit (moms = brutto − netto)

Refunds (`paid to shopify`) reverserar splitten med samma logik.

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py usd
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\usd\WISE_USD_STANDALONE.se"
```

## Status Q1 2026
- 83 verifikat, DEB=CRED=603 211,43 SEK
- 3051 netto = 923,98 SEK · 2611 moms = 230,99 SEK · brutto = 1 154,97 SEK ✅
