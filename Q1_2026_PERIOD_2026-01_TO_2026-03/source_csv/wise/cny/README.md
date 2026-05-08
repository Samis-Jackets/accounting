# Hur du gör (snabbreferens)

Se den fullständiga metodiken här:
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `..\usd\METHODOLOGY_USD.md` (utfört exempel med beslut)

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py cny
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\cny\WISE_CNY_STANDALONE.se"
```

## Vad ska finnas i mappen efter körning
1. `statement_*.csv` (källan från Wise)
2. `cny_brain_dump.txt` (dina overrides)
3. `WISE_CNY_AUDIT.md` (revisor-MD)
4. `WISE_CNY_STANDALONE.se` (Visma-upload)
5. `METHODOLOGY_CNY.md` (dina beslut – kopiera USD-mallen)
