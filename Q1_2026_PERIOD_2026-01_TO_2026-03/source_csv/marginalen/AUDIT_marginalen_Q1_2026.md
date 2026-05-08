# 📂 marginalen — Audit Q1 2026 (Samis Jackets AB)

**Period:** 2026-01-01 → 2026-03-31  |  **Genererad:** 2026-04-29
**Föreslaget bankkonto:** 1930 (Marginalen företagskonto)

## 1. Källfiler i denna mapp

Följande råfiler från banken låg i denna mapp och bearbetades av `build_audit_csv.py`. Räkna gärna manuellt i CSV:erna och jämför kolumnen *Rader i råfilen* mot *Inlästa transaktioner*.

| Råfil | Rader i råfilen (datalinjer) | Inlästa transaktioner |
|---|---:|---:|
| AUDIT_marginalen_Q1_2026.csv | 123 | 0 ⚠️ (kontrollera) |
| Marginalen 2026-01-01-2026-03-31.csv | 124 | 123 ⚠️ (kontrollera) |
| **TOTALT** | — | **123** |

> ⚠️ Skillnad i antal raden kan bero på filtrering av rubrik-/summarader. Alla rubrik-/summarader hoppas över medvetet.

## 2. Kontrolltotaler

- **IN (insättningar):** 387 673,62 SEK
- **UT (uttag):** -413 193,28 SEK
- **Netto perioden:** -25 519,66 SEK
- **Antal needs_review:** 0

## 3. Sammanställning per kategori

| Kategori | Konto(n) | Antal | Summa SEK |
|---|---|---:|---:|
| WORLDLINE_PAYOUT_TO_1930 | 1947 | 57 | 194 159,97 |
| INTERNAL_WISE | 1944 | 3 | -116 620,00 |
| SALARY | 7210 | 5 | -81 507,00 |
| FREIGHT | 5700 | 20 | -81 209,28 |
| EXPORT_NORWAY_NO_VAT | 3105 | 3 | 58 000,00 |
| TAX | 1630 | 1 | -52 871,00 |
| SALES_FALLBACK | 3051 | 2 | 49 668,00 |
| OWNER_LOAN_2893_NORDEA | 2893 | 13 | 45 960,65 |
| RENT | 5010 | 2 | -20 836,00 |
| VARUINKOP_PRIVAT | 4010 | 1 | -12 500,00 |
| SALES | 3051 | 3 | 11 889,00 |
| FORBRUK_FALLBACK | 5460 | 1 | -11 800,00 |
| INSURANCE_NO_VAT | 6310 | 2 | -4 633,00 |
| MOBILE_SUBSCRIPTION | 6212 | 3 | -1 707,00 |
| TERMINAL_FEE | 6570 | 3 | -744,00 |
| PARKING_TRAVEL | 5800 | 1 | -560,00 |
| BANK_FEE | 6570 | 3 | -210,00 |

## 4. Sammanställning per BAS-konto (motkonto)

| Konto | Namn | Antal | Summa SEK |
|---|---|---:|---:|
| 1947 | Worldline | 57 | 194 159,97 |
| 1944 | Wise EUR | 3 | -116 620,00 |
| 7210 |  | 5 | -81 507,00 |
| 5700 |  | 20 | -81 209,28 |
| 3051 | Försäljning Shopify/Swish 25% | 5 | 61 557,00 |
| 3105 |  | 3 | 58 000,00 |
| 1630 |  | 1 | -52 871,00 |
| 2893 | Skuld till närstående (Sami) | 13 | 45 960,65 |
| 5010 |  | 2 | -20 836,00 |
| 4010 |  | 1 | -12 500,00 |
| 5460 | Förbrukningsmaterial | 1 | -11 800,00 |
| 6310 | Företagsförsäkring | 2 | -4 633,00 |
| 6212 | Mobiltelefon | 3 | -1 707,00 |
| 6570 | Bankkostnader | 6 | -954,00 |
| 5800 |  | 1 | -560,00 |

## 5. Alla 123 transaktioner (kronologiskt)

Markera rader med ⚠️ → behöver din bekräftelse innan SE-fil byggs.

| # | Datum | SEK | Original | R | Konto | Kategori | Motpart / Beskrivning | Anledning | ⚠️ |
|---:|---|---:|---:|:---:|:---:|---|---|---|:---:|
| 1 | 2026-01-01 | -70.00 |  | O | 6570 | BANK_FEE | Månadsavgift Företagskonto |  |  |
| 2 | 2026-01-02 | 13764.63 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B12319685833 | Worldline payout (B-rad) -> intern överförin… |  |
| 3 | 2026-01-02 | 3411.61 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01019707261 | Worldline payout (B-rad) -> intern överförin… |  |
| 4 | 2026-01-05 | 4525.12 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01059767400 | Worldline payout (B-rad) -> intern överförin… |  |
| 5 | 2026-01-07 | 4274.49 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01079801854 | Worldline payout (B-rad) -> intern överförin… |  |
| 6 | 2026-01-07 | 5187.01 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01069781423 | Worldline payout (B-rad) -> intern överförin… |  |
| 7 | 2026-01-07 | 12385.00 |  | I | 3051 | SALES | Swish sales lunar |  |  |
| 8 | 2026-01-07 | -248.00 |  | O | 6570 | TERMINAL_FEE | 3306016 — card terminal |  |  |
| 9 | 2026-01-08 | 4983.26 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01089820788 | Worldline payout (B-rad) -> intern överförin… |  |
| 10 | 2026-01-08 | 2600.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — ÖVERFÖRING |  |  |
| 11 | 2026-01-08 | -85720.00 |  | O | 1944 | INTERNAL_WISE | 55250500 — Till wise |  |  |
| 12 | 2026-01-09 | 1882.69 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01099844174 | Worldline payout (B-rad) -> intern överförin… |  |
| 13 | 2026-01-09 | -7500.00 |  | O | 1944 | INTERNAL_WISE | 55250500 — WISE EUROPE SA |  |  |
| 14 | 2026-01-12 | 1294.00 |  | I | 3051 | SALES_FALLBACK | 6641229 — 0006641229 |  |  |
| 15 | 2026-01-12 | 2230.42 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01129913847 | Worldline payout (B-rad) -> intern överförin… |  |
| 16 | 2026-01-12 | 3068.93 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01119895474 | Worldline payout (B-rad) -> intern överförin… |  |
| 17 | 2026-01-12 | 1235.93 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01109871141 | Worldline payout (B-rad) -> intern överförin… |  |
| 18 | 2026-01-12 | -1863.00 |  | O | 5700 | FREIGHT | 9423047 — SCHENKER AB |  |  |
| 19 | 2026-01-12 | -82.00 |  | O | 5700 | FREIGHT | 9423047 — SCHENKER AB |  |  |
| 20 | 2026-01-14 | 1867.58 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01149951988 | Worldline payout (B-rad) -> intern överförin… |  |
| 21 | 2026-01-15 | 396.41 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01159978317 | Worldline payout (B-rad) -> intern överförin… |  |
| 22 | 2026-01-16 | 7048.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWISH SALES |  |  |
| 23 | 2026-01-16 | 1848.92 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01160005483 | Worldline payout (B-rad) -> intern överförin… |  |
| 24 | 2026-01-16 | 637.65 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — Privat konto |  |  |
| 25 | 2026-01-19 | 1066.07 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01190076678 | Worldline payout (B-rad) -> intern överförin… |  |
| 26 | 2026-01-19 | -569.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | 47460035 — Mobil abbonmang |  |  |
| 27 | 2026-01-19 | 1978.25 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01170031005 | Worldline payout (B-rad) -> intern överförin… |  |
| 28 | 2026-01-20 | 394.14 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01200091424 | Worldline payout (B-rad) -> intern överförin… |  |
| 29 | 2026-01-21 | 1484.31 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01210114816 | Worldline payout (B-rad) -> intern överförin… |  |
| 30 | 2026-01-21 | -560.00 |  | O | 5800 | PARKING_TRAVEL | 9453036 — Parkirng |  |  |
| 31 | 2026-01-22 | 1368.96 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01220140280 | Worldline payout (B-rad) -> intern överförin… |  |
| 32 | 2026-01-22 | -23400.00 |  | O | 1944 | INTERNAL_WISE | 55250500 — Wise |  |  |
| 33 | 2026-01-26 | 3031.64 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01260240243 | Worldline payout (B-rad) -> intern överförin… |  |
| 34 | 2026-01-26 | 5249.78 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01240194434 | Worldline payout (B-rad) -> intern överförin… |  |
| 35 | 2026-01-27 | 2350.63 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01270256020 | Worldline payout (B-rad) -> intern överförin… |  |
| 36 | 2026-01-27 | -248.00 |  | O | 6570 | TERMINAL_FEE | 3306016 — Card terminal |  |  |
| 37 | 2026-01-27 | -171.00 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 38 | 2026-01-27 | -2016.00 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 39 | 2026-01-27 | -275.00 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 40 | 2026-01-27 | -94.71 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 41 | 2026-01-27 | -94.00 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 42 | 2026-01-27 | -2170.00 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 43 | 2026-01-27 | -171.74 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 44 | 2026-01-27 | -78.83 |  | O | 5700 | FREIGHT | 9423047 — Frakt |  |  |
| 45 | 2026-01-27 | -3000.00 |  | O | 2893 | OWNER_LOAN_2893_NORDEA | 30860059626 — 2893 återbetalning |  |  |
| 46 | 2026-01-28 | 1570.73 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01280278972 | Worldline payout (B-rad) -> intern överförin… |  |
| 47 | 2026-01-29 | 4064.41 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01290305116 | Worldline payout (B-rad) -> intern överförin… |  |
| 48 | 2026-02-01 | -70.00 |  | O | 6570 | BANK_FEE | Månadsavgift Företagskonto |  |  |
| 49 | 2026-02-02 | 3845.85 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02020405609 | Worldline payout (B-rad) -> intern överförin… |  |
| 50 | 2026-02-02 | -12500.00 |  | O | 4010 | VARUINKOP_PRIVAT | 842446945339122 — Inköp från privatperson kläder |  |  |
| 51 | 2026-02-02 | 5.48 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02010386401 | Worldline payout (B-rad) -> intern överförin… |  |
| 52 | 2026-02-02 | 9927.88 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B01310359414 | Worldline payout (B-rad) -> intern överförin… |  |
| 53 | 2026-02-03 | 837.53 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02030422253 | Worldline payout (B-rad) -> intern överförin… |  |
| 54 | 2026-02-04 | 1259.77 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02040445787 | Worldline payout (B-rad) -> intern överförin… |  |
| 55 | 2026-02-05 | 1752.54 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02050471530 | Worldline payout (B-rad) -> intern överförin… |  |
| 56 | 2026-02-05 | -1556.00 |  | O | 5700 | FREIGHT | 5328653 — Frakt |  |  |
| 57 | 2026-02-06 | 502.72 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02060497853 | Worldline payout (B-rad) -> intern överförin… |  |
| 58 | 2026-02-06 | 13104.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWISH SALES |  |  |
| 59 | 2026-02-09 | 3697.82 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02090569951 | Worldline payout (B-rad) -> intern överförin… |  |
| 60 | 2026-02-09 | 3591.33 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02070523538 | Worldline payout (B-rad) -> intern överförin… |  |
| 61 | 2026-02-10 | 4547.93 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02100584482 | Worldline payout (B-rad) -> intern överförin… |  |
| 62 | 2026-02-10 | 7500.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — Insättning |  |  |
| 63 | 2026-02-11 | 1376.95 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02110607269 | Worldline payout (B-rad) -> intern överförin… |  |
| 64 | 2026-02-11 | -569.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | 47460035 — Abbonmang |  |  |
| 65 | 2026-02-11 | -15627.00 |  | O | 5010 | RENT | 4392007 — Lagar hyra 12/2025. 1-2 2026 |  |  |
| 66 | 2026-02-11 | -2100.00 |  | O | 5700 | FREIGHT | 5328653 — DSV ROAD AB |  |  |
| 67 | 2026-02-13 | 3004.71 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02130658937 | Worldline payout (B-rad) -> intern överförin… |  |
| 68 | 2026-02-16 | -1192.00 |  | O | 5700 | FREIGHT | 5328653 — Frakt |  |  |
| 69 | 2026-02-16 | 546.42 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02150711570 | Worldline payout (B-rad) -> intern överförin… |  |
| 70 | 2026-02-16 | 958.62 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02140685830 | Worldline payout (B-rad) -> intern överförin… |  |
| 71 | 2026-02-17 | 1317.38 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02170746228 | Worldline payout (B-rad) -> intern överförin… |  |
| 72 | 2026-02-18 | 18000.00 |  | I | 3105 | EXPORT_NORWAY_NO_VAT | Mohamad Sharif A Qalaji |  |  |
| 73 | 2026-02-18 | 297.06 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02180770543 | Worldline payout (B-rad) -> intern överförin… |  |
| 74 | 2026-02-19 | 28000.00 |  | I | 3105 | EXPORT_NORWAY_NO_VAT | CI-2026-001 |  |  |
| 75 | 2026-02-19 | 2308.90 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02190795628 | Worldline payout (B-rad) -> intern överförin… |  |
| 76 | 2026-02-19 | -46372.00 |  | O | 5700 | FREIGHT | 6797542 — UNITRANS SHIPPING & TRANSPORT AB |  |  |
| 77 | 2026-02-20 | 12000.00 |  | I | 3105 | EXPORT_NORWAY_NO_VAT | CI-2026-001 |  |  |
| 78 | 2026-02-20 | 375.55 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02200821451 | Worldline payout (B-rad) -> intern överförin… |  |
| 79 | 2026-02-23 | 1579.49 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02210847561 | Worldline payout (B-rad) -> intern överförin… |  |
| 80 | 2026-02-24 | -20000.00 |  | O | 2893 | OWNER_LOAN_2893_NORDEA | 30860059626 — Till 2893 |  |  |
| 81 | 2026-02-24 | 3889.36 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02240904331 | Worldline payout (B-rad) -> intern överförin… |  |
| 82 | 2026-02-24 | -16725.00 |  | O | 7210 | SALARY | 825785842031717 — Mari Lön januari |  |  |
| 83 | 2026-02-24 | -15916.00 |  | O | 7210 | SALARY | 90236807120 — Emelie LÖN JANUARI 2026 |  |  |
| 84 | 2026-02-24 | -522.00 |  | O | 5700 | FREIGHT | 5328653 — Frakt |  |  |
| 85 | 2026-02-25 | -4500.00 |  | O | 2893 | OWNER_LOAN_2893_NORDEA | 34690055203 — Till 2893 |  |  |
| 86 | 2026-02-25 | 48374.00 |  | I | 3051 | SALES_FALLBACK | 6641229 — 0006641229 |  |  |
| 87 | 2026-02-27 | 5118.52 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02270977337 | Worldline payout (B-rad) -> intern överförin… |  |
| 88 | 2026-02-27 | -19612.00 |  | O | 7210 | SALARY | 50501055 — Emelie och Mari skrattar |  |  |
| 89 | 2026-02-27 | -871.00 |  | O | 6310 | INSURANCE_NO_VAT | 7277536 — Bil försäkring |  |  |
| 90 | 2026-02-27 | -5209.00 |  | O | 5010 | RENT | 4392007 — Fastighets AB Akvarium |  |  |
| 91 | 2026-03-01 | -70.00 |  | O | 6570 | BANK_FEE | Månadsavgift Företagskonto |  |  |
| 92 | 2026-03-02 | 841.50 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03021053599 | Worldline payout (B-rad) -> intern överförin… |  |
| 93 | 2026-03-02 | 0.99 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B02281005989 | Worldline payout (B-rad) -> intern överförin… |  |
| 94 | 2026-03-02 | -248.00 |  | O | 6570 | TERMINAL_FEE | 47704044 — SVEA BANK AB REF 9 |  |  |
| 95 | 2026-03-02 | -5299.00 |  | O | 5700 | FREIGHT | 5328653 — Norge frakt utan moms |  |  |
| 96 | 2026-03-02 | -949.00 |  | O | 5700 | FREIGHT | 5328653 — Frakt |  |  |
| 97 | 2026-03-05 | 98.36 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03051119511 | Worldline payout (B-rad) -> intern överförin… |  |
| 98 | 2026-03-09 | -748.00 |  | O | 5700 | FREIGHT | 5328653 — DSV Road AB |  |  |
| 99 | 2026-03-11 | -569.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | 47460035 — Mobile abbonmang |  |  |
| 100 | 2026-03-16 | 3957.86 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03161387133 | Worldline payout (B-rad) -> intern överförin… |  |
| 101 | 2026-03-16 | 1645.10 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03151367841 | Worldline payout (B-rad) -> intern överförin… |  |
| 102 | 2026-03-17 | 8560.72 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03171403665 | Worldline payout (B-rad) -> intern överförin… |  |
| 103 | 2026-03-17 | 21911.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWEISH SALES |  |  |
| 104 | 2026-03-18 | -52871.00 |  | O | 1630 | TAX | 50501055 — moms ocha rbetsgivare |  |  |
| 105 | 2026-03-20 | 5981.19 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03201480621 | Worldline payout (B-rad) -> intern överförin… |  |
| 106 | 2026-03-23 | 6665.46 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03221536484 | Worldline payout (B-rad) -> intern överförin… |  |
| 107 | 2026-03-24 | 12504.29 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03241573073 | Worldline payout (B-rad) -> intern överförin… |  |
| 108 | 2026-03-25 | 2520.52 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03251597946 | Worldline payout (B-rad) -> intern överförin… |  |
| 109 | 2026-03-25 | 7460.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWISH SALES |  |  |
| 110 | 2026-03-25 | -5501.00 |  | O | 7210 | SALARY | 825785842031717 — Lön fabruari och januari |  |  |
| 111 | 2026-03-25 | -11800.00 |  | O | 5460 | FORBRUK_FALLBACK | 810349647607374 — Betalningen för sista fakturan |  |  |
| 112 | 2026-03-26 | -23753.00 |  | O | 7210 | SALARY | 90236807120 — Februari lön och semesteremile |  |  |
| 113 | 2026-03-26 | 7624.60 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03261624898 | Worldline payout (B-rad) -> intern överförin… |  |
| 114 | 2026-03-27 | 5674.45 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03271651166 | Worldline payout (B-rad) -> intern överförin… |  |
| 115 | 2026-03-27 | -1150.00 |  | O | 5700 | FREIGHT | 5328653 — Frakt |  |  |
| 116 | 2026-03-30 | 16107.20 |  | I | 1947 | WORLDLINE_PAYOUT_TO_1… | 92356405879 — B03301727484 | Worldline payout (B-rad) -> intern överförin… |  |
| 117 | 2026-03-30 | 4400.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWISH SALES |  |  |
| 118 | 2026-03-30 | 3000.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — SWISH SALES |  |  |
| 119 | 2026-03-30 | 5800.00 |  | I | 2893 | OWNER_LOAN_2893_NORDEA | 92356405879 — FROM 2893 |  |  |
| 120 | 2026-03-30 | -248.00 |  | O | 3051 | SALES | 47704044 — Kort terminal |  |  |
| 121 | 2026-03-30 | -248.00 |  | O | 3051 | SALES | 47704044 — Kort terminal |  |  |
| 122 | 2026-03-30 | -3762.00 |  | O | 6310 | INSURANCE_NO_VAT | 53020525 — Försäkring |  |  |
| 123 | 2026-03-31 | -14305.00 |  | O | 5700 | FREIGHT | 53971826 — Container shipping to Eskilstu |  |  |

---
_Genererad av `build_per_bank_audit.py` från `AUDIT_Q1_2026_FILL_REASONS.csv`._