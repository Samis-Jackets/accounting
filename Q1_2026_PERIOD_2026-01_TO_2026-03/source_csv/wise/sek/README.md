# Hur du gör (snabbreferens)

Se den fullständiga metodiken här:
- `..\..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `..\usd\METHODOLOGY_USD.md` (utfört exempel med beslut)

## Wise SEK är INTE en försäljnings-bank
Försäljning bokas redan på första landingen (Lunar/Marginalen/Worldline).
- `Received money from Samis Jackets AB / Swish sales` → **1948** (intern, ej moms)
- `Topped up account` (från Nordea privat) → **2893** (ägarinsättning)

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py sek
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\sek\WISE_SEK_STANDALONE.se"
```

## Vad ska finnas i mappen efter körning
1. `statement_*.csv` (källan från Wise)
2. `sek_brain_dump.txt` (dina overrides)
3. `WISE_SEK_AUDIT.md` (revisor-MD)
4. `WISE_SEK_STANDALONE.se` (Visma-upload)
5. `METHODOLOGY_SEK.md` (dina beslut – kopiera USD-mallen)
