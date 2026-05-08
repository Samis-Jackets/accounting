# Hur du gör (snabbreferens)

Se den fullständiga metodiken här:
- `..\..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik B2C 25 %
- `..\..\..\METHODOLOGY.md` (huvudfil)
- `..\usd\METHODOLOGY_USD.md` (utfört exempel med beslut)

## Försäljning B2C 25 % (Stripe → Shopify EU-kunder)
Alla `Received money from STRIPE`-rader är försäljning från EU-kunder.
Brutto bokas på 1944, splittas auto:
- **3056** Försäljning varor EU 25 %  (= brutto/1.25)
- **2611** Utgående moms 25 %  (= brutto − netto)

## 3 kommandon
```powershell
cd ..\..\..
..\.venv\Scripts\python.exe analyze_wise_currency.py eur
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\eur\WISE_EUR_STANDALONE.se"
```

## Vad ska finnas i mappen efter körning
1. `statement_*.csv` (källan från Wise)
2. `eur_brain_dump.txt` (dina overrides)
3. `WISE_EUR_AUDIT.md` (revisor-MD)
4. `WISE_EUR_STANDALONE.se` (Visma-upload)
5. `METHODOLOGY_EUR.md` (dina beslut – kopiera USD-mallen)
