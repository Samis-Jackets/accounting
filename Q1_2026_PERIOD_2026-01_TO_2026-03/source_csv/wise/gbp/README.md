# Hur du gör (snabbreferens)

Se den fullständiga metodiken här:
- `..\..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `..\usd\METHODOLOGY_USD.md` (utfört exempel med beslut)

## Försäljning B2C 25 % (om Stripe GBP payouts)
Vid Stripe payouts från UK-kunder: brutto på 1943, splittas via 3105 (export)
eller 3001+2611 om kunden klassas som EU-moms.
Q1 2026: bara 2 ver (Convert + Loan från ägaren). Inga sales-rader.

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py gbp
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\gbp\WISE_GBP_STANDALONE.se"
```

## Vad ska finnas i mappen efter körning
1. `statement_*.csv` (källan från Wise)
2. `gbp_brain_dump.txt` (dina overrides)
3. `WISE_GBP_AUDIT.md` (revisor-MD)
4. `WISE_GBP_STANDALONE.se` (Visma-upload)
5. `METHODOLOGY_GBP.md` (dina beslut – kopiera USD-mallen)
