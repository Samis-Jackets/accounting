# 📂 worldline — Audit Q1 2026 (Samis Jackets AB)

**Period:** 2026-01-01 → 2026-03-31  |  **Genererad:** 2026-04-29
**Föreslaget bankkonto:** 1947 (Worldline)

## 1. Källfiler i denna mapp

Följande råfiler från banken låg i denna mapp och bearbetades av `build_audit_csv.py`. Räkna gärna manuellt i CSV:erna och jämför kolumnen *Rader i råfilen* mot *Inlästa transaktioner*.

| Råfil | Rader i råfilen (datalinjer) | Inlästa transaktioner |
|---|---:|---:|
| AUDIT_worldline_Q1_2026.csv | 111 | 0 ⚠️ (kontrollera) |
| monthly_report_202601.xlsx | 24 | 46 ⚠️ (kontrollera) |
| monthly_report_202602.xlsx | 24 | 41 ⚠️ (kontrollera) |
| monthly_report_202603.xlsx | 24 | 24 ✅ |
| **TOTALT** | — | **111** |

> ⚠️ Skillnad i antal raden kan bero på filtrering av rubrik-/summarader. Alla rubrik-/summarader hoppas över medvetet.

## 2. Kontrolltotaler

- **IN (insättningar):** 181 663,44 SEK
- **UT (uttag):** -1 278,57 SEK
- **Netto perioden:** 180 384,87 SEK
- **Antal needs_review:** 0

## 3. Sammanställning per kategori

| Kategori | Konto(n) | Antal | Summa SEK |
|---|---|---:|---:|
| SALES | 3051 | 56 | 181 663,44 |
| BANK_FEE | 6570 | 55 | -1 278,57 |

## 4. Sammanställning per BAS-konto (motkonto)

| Konto | Namn | Antal | Summa SEK |
|---|---|---:|---:|
| 3051 | Försäljning Shopify/Swish 25% | 56 | 181 663,44 |
| 6570 | Bankkostnader | 55 | -1 278,57 |

## 5. Alla 111 transaktioner (kronologiskt)

Markera rader med ⚠️ → behöver din bekräftelse innan SE-fil byggs.

| # | Datum | SEK | Original | R | Konto | Kategori | Motpart / Beskrivning | Anledning | ⚠️ |
|---:|---|---:|---:|:---:|:---:|---|---|---|:---:|
| 1 | 2026-01-01 | 3433.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01019707261 (… | REF=B01019707261 matchar Marginalen B-rad 34… |  |
| 2 | 2026-01-01 | -26.38 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01019… |  |  |
| 3 | 2026-01-05 | 4555.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01059767400 (… | REF=B01059767400 matchar Marginalen B-rad 45… |  |
| 4 | 2026-01-05 | -29.88 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01059… |  |  |
| 5 | 2026-01-06 | 5221.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01069781423 (… | REF=B01069781423 matchar Marginalen B-rad 51… |  |
| 6 | 2026-01-06 | -33.99 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01069… |  |  |
| 7 | 2026-01-07 | 4303.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01079801854 (… | REF=B01079801854 matchar Marginalen B-rad 42… |  |
| 8 | 2026-01-07 | -28.51 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01079… |  |  |
| 9 | 2026-01-08 | 5016.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01089820788 (… | REF=B01089820788 matchar Marginalen B-rad 49… |  |
| 10 | 2026-01-08 | -32.74 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01089… |  |  |
| 11 | 2026-01-09 | 1895.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01099844174 (… | REF=B01099844174 matchar Marginalen B-rad 18… |  |
| 12 | 2026-01-09 | -12.31 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01099… |  |  |
| 13 | 2026-01-10 | 1244.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01109871141 (… | REF=B01109871141 matchar Marginalen B-rad 12… |  |
| 14 | 2026-01-10 | -8.07 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01109… |  |  |
| 15 | 2026-01-11 | 3089.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01119895474 (… | REF=B01119895474 matchar Marginalen B-rad 30… |  |
| 16 | 2026-01-11 | -20.07 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01119… |  |  |
| 17 | 2026-01-12 | 2245.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01129913847 (… | REF=B01129913847 matchar Marginalen B-rad 22… |  |
| 18 | 2026-01-12 | -14.58 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01129… |  |  |
| 19 | 2026-01-14 | 1880.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01149951988 (… | REF=B01149951988 matchar Marginalen B-rad 18… |  |
| 20 | 2026-01-14 | -12.42 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01149… |  |  |
| 21 | 2026-01-15 | 399.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01159978317 (… | REF=B01159978317 matchar Marginalen B-rad 39… |  |
| 22 | 2026-01-15 | -2.59 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01159… |  |  |
| 23 | 2026-01-16 | 1861.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01160005483 (… | REF=B01160005483 matchar Marginalen B-rad 18… |  |
| 24 | 2026-01-16 | -12.08 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01160… |  |  |
| 25 | 2026-01-17 | 1997.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01170031005 (… | REF=B01170031005 matchar Marginalen B-rad 19… |  |
| 26 | 2026-01-17 | -18.75 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01170… |  |  |
| 27 | 2026-01-19 | 1075.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01190076678 (… | REF=B01190076678 matchar Marginalen B-rad 10… |  |
| 28 | 2026-01-19 | -8.93 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01190… |  |  |
| 29 | 2026-01-20 | 398.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01200091424 (… | REF=B01200091424 matchar Marginalen B-rad 39… |  |
| 30 | 2026-01-20 | -3.86 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01200… |  |  |
| 31 | 2026-01-21 | 1494.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01210114816 (… | REF=B01210114816 matchar Marginalen B-rad 14… |  |
| 32 | 2026-01-21 | -9.69 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01210… |  |  |
| 33 | 2026-01-22 | 1378.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01220140280 (… | REF=B01220140280 matchar Marginalen B-rad 13… |  |
| 34 | 2026-01-22 | -9.04 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01220… |  |  |
| 35 | 2026-01-24 | 5284.44 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01240194434 (… | REF=B01240194434 matchar Marginalen B-rad 52… |  |
| 36 | 2026-01-24 | -34.66 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01240… |  |  |
| 37 | 2026-01-26 | 3073.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01260240243 (… | REF=B01260240243 matchar Marginalen B-rad 30… |  |
| 38 | 2026-01-26 | -41.36 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01260… |  |  |
| 39 | 2026-01-27 | 2366.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01270256020 (… | REF=B01270256020 matchar Marginalen B-rad 23… |  |
| 40 | 2026-01-27 | -15.37 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01270… |  |  |
| 41 | 2026-01-28 | 1581.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01280278972 (… | REF=B01280278972 matchar Marginalen B-rad 15… |  |
| 42 | 2026-01-28 | -10.27 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01280… |  |  |
| 43 | 2026-01-29 | 4091.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01290305116 (… | REF=B01290305116 matchar Marginalen B-rad 40… |  |
| 44 | 2026-01-29 | -26.59 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01290… |  |  |
| 45 | 2026-01-31 | 9993.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B01310359414 (… | REF=B01310359414 matchar Marginalen B-rad 99… |  |
| 46 | 2026-01-31 | -65.12 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B01310… |  |  |
| 47 | 2026-02-01 | 0.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02010386401 (… | REF=B02010386401 matchar Marginalen B-rad 5.… |  |
| 48 | 2026-02-02 | 3871.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02020405609 (… | REF=B02020405609 matchar Marginalen B-rad 38… |  |
| 49 | 2026-02-02 | -25.15 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02020… |  |  |
| 50 | 2026-02-03 | 843.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02030422253 (… | REF=B02030422253 matchar Marginalen B-rad 83… |  |
| 51 | 2026-02-03 | -5.47 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02030… |  |  |
| 52 | 2026-02-04 | 1268.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02040445787 (… | REF=B02040445787 matchar Marginalen B-rad 12… |  |
| 53 | 2026-02-04 | -8.23 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02040… |  |  |
| 54 | 2026-02-05 | 1764.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02050471530 (… | REF=B02050471530 matchar Marginalen B-rad 17… |  |
| 55 | 2026-02-05 | -11.46 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02050… |  |  |
| 56 | 2026-02-06 | 506.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02060497853 (… | REF=B02060497853 matchar Marginalen B-rad 50… |  |
| 57 | 2026-02-06 | -3.28 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02060… |  |  |
| 58 | 2026-02-07 | 3615.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02070523538 (… | REF=B02070523538 matchar Marginalen B-rad 35… |  |
| 59 | 2026-02-07 | -23.67 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02070… |  |  |
| 60 | 2026-02-09 | 3722.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02090569951 (… | REF=B02090569951 matchar Marginalen B-rad 36… |  |
| 61 | 2026-02-09 | -24.18 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02090… |  |  |
| 62 | 2026-02-10 | 4581.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02100584482 (… | REF=B02100584482 matchar Marginalen B-rad 45… |  |
| 63 | 2026-02-10 | -33.07 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02100… |  |  |
| 64 | 2026-02-11 | 1386.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02110607269 (… | REF=B02110607269 matchar Marginalen B-rad 13… |  |
| 65 | 2026-02-11 | -9.05 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02110… |  |  |
| 66 | 2026-02-13 | 3038.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02130658937 (… | REF=B02130658937 matchar Marginalen B-rad 30… |  |
| 67 | 2026-02-13 | -33.29 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02130… |  |  |
| 68 | 2026-02-14 | 965.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02140685830 (… | REF=B02140685830 matchar Marginalen B-rad 95… |  |
| 69 | 2026-02-14 | -6.38 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02140… |  |  |
| 70 | 2026-02-15 | 550.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02150711570 (… | REF=B02150711570 matchar Marginalen B-rad 54… |  |
| 71 | 2026-02-15 | -3.58 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02150… |  |  |
| 72 | 2026-02-17 | 1326.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02170746228 (… | REF=B02170746228 matchar Marginalen B-rad 13… |  |
| 73 | 2026-02-17 | -8.62 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02170… |  |  |
| 74 | 2026-02-18 | 299.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02180770543 (… | REF=B02180770543 matchar Marginalen B-rad 29… |  |
| 75 | 2026-02-18 | -1.94 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02180… |  |  |
| 76 | 2026-02-19 | 2324.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02190795628 (… | REF=B02190795628 matchar Marginalen B-rad 23… |  |
| 77 | 2026-02-19 | -15.10 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02190… |  |  |
| 78 | 2026-02-20 | 378.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02200821451 (… | REF=B02200821451 matchar Marginalen B-rad 37… |  |
| 79 | 2026-02-20 | -2.45 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02200… |  |  |
| 80 | 2026-02-21 | 1590.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02210847561 (… | REF=B02210847561 matchar Marginalen B-rad 15… |  |
| 81 | 2026-02-21 | -10.51 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02210… |  |  |
| 82 | 2026-02-24 | 3915.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02240904331 (… | REF=B02240904331 matchar Marginalen B-rad 38… |  |
| 83 | 2026-02-24 | -25.64 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02240… |  |  |
| 84 | 2026-02-27 | 5152.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02270977337 (… | REF=B02270977337 matchar Marginalen B-rad 51… |  |
| 85 | 2026-02-27 | -33.48 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02270… |  |  |
| 86 | 2026-02-28 | 1.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B02281005989 (… | REF=B02281005989 matchar Marginalen B-rad 0.… |  |
| 87 | 2026-02-28 | -0.01 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B02281… |  |  |
| 88 | 2026-03-02 | 847.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03021053599 (… | REF=B03021053599 matchar Marginalen B-rad 84… |  |
| 89 | 2026-03-02 | -5.50 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03021… |  |  |
| 90 | 2026-03-05 | 99.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03051119511 (… | REF=B03051119511 matchar Marginalen B-rad 98… |  |
| 91 | 2026-03-05 | -0.64 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03051… |  |  |
| 92 | 2026-03-15 | 1656.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03151367841 (… | REF=B03151367841 matchar Marginalen B-rad 16… |  |
| 93 | 2026-03-15 | -10.90 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03151… |  |  |
| 94 | 2026-03-16 | 3985.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03161387133 (… | REF=B03161387133 matchar Marginalen B-rad 39… |  |
| 95 | 2026-03-16 | -27.14 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03161… |  |  |
| 96 | 2026-03-17 | 8619.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03171403665 (… | REF=B03171403665 matchar Marginalen B-rad 85… |  |
| 97 | 2026-03-17 | -58.28 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03171… |  |  |
| 98 | 2026-03-20 | 6021.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03201480621 (… | REF=B03201480621 matchar Marginalen B-rad 59… |  |
| 99 | 2026-03-20 | -39.81 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03201… |  |  |
| 100 | 2026-03-22 | 6721.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03221536484 (… | REF=B03221536484 matchar Marginalen B-rad 66… |  |
| 101 | 2026-03-22 | -55.54 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03221… |  |  |
| 102 | 2026-03-24 | 12591.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03241573073 (… | REF=B03241573073 matchar Marginalen B-rad 12… |  |
| 103 | 2026-03-24 | -86.71 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03241… |  |  |
| 104 | 2026-03-25 | 2537.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03251597946 (… | REF=B03251597946 matchar Marginalen B-rad 25… |  |
| 105 | 2026-03-25 | -16.48 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03251… |  |  |
| 106 | 2026-03-26 | 7690.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03261624898 (… | REF=B03261624898 matchar Marginalen B-rad 76… |  |
| 107 | 2026-03-26 | -65.40 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03261… |  |  |
| 108 | 2026-03-27 | 5719.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03271651166 (… | REF=B03271651166 matchar Marginalen B-rad 56… |  |
| 109 | 2026-03-27 | -44.55 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03271… |  |  |
| 110 | 2026-03-30 | 16213.00 |  | I | 3051 | SALES | G&S By Samis jackets — Worldline payout B03301727484 (… | REF=B03301727484 matchar Marginalen B-rad 16… |  |
| 111 | 2026-03-30 | -105.80 |  | O | 6570 | BANK_FEE | Worldline / Bambora — Worldline avgifter payout B03301… |  |  |

---
_Genererad av `build_per_bank_audit.py` från `AUDIT_Q1_2026_FILL_REASONS.csv`._