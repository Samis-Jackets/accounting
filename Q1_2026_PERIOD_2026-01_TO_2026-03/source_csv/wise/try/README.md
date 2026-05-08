# Hur du gör (snabbreferens)

Se den fullständiga metodiken här:
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `..\usd\METHODOLOGY_USD.md` (utfört exempel med beslut)

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py try
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\try\WISE_TRY_STANDALONE.se"
```

## Vad ska finnas i mappen efter körning
1. `statement_*.csv` (källan från Wise)
2. `try_brain_dump.txt` (dina overrides)
3. `WISE_TRY_AUDIT.md` (revisor-MD)
4. `WISE_TRY_STANDALONE.se` (Visma-upload)
5. `METHODOLOGY_TRY.md` (dina beslut – kopiera USD-mallen)
