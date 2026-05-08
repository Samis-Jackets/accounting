# 📂 nordea — Audit Q1 2026 (Samis Jackets AB)

**Period:** 2026-01-01 → 2026-03-31  |  **Genererad:** 2026-04-29
**Föreslaget bankkonto:** 2893 (Skuld till närstående (Sami))

## 1. Källfiler i denna mapp

Följande råfiler från banken låg i denna mapp och bearbetades av `build_audit_csv.py`. Räkna gärna manuellt i CSV:erna och jämför kolumnen *Rader i råfilen* mot *Inlästa transaktioner*.

| Råfil | Rader i råfilen (datalinjer) | Inlästa transaktioner |
|---|---:|---:|
| AUDIT_nordea_Q1_2026.csv | 175 | 0 ⚠️ (kontrollera) |
| Nordea Gold - 2026-04-28 14.15.07.csv | 39 | 39 ✅ |
| Nordea Premium - 2026-04-28 13.07.07.csv | 30 | 30 ✅ |
| PERSONKONTO-STUDENT 3086 00 59626 - 2026-04-28 12.40.41.csv | 106 | 106 ✅ |
| **TOTALT** | — | **175** |

> ⚠️ Skillnad i antal raden kan bero på filtrering av rubrik-/summarader. Alla rubrik-/summarader hoppas över medvetet.

## 2. Kontrolltotaler

- **IN (insättningar):** 195 366,26 SEK
- **UT (uttag):** -190 653,19 SEK
- **Netto perioden:** 4 713,07 SEK
- **Antal needs_review:** 0

## 3. Sammanställning per kategori

| Kategori | Konto(n) | Antal | Summa SEK |
|---|---|---:|---:|
| SALES | 3051 | 21 | 40 020,00 |
| CASH_WITHDRAWAL | 1910 | 15 | -31 500,00 |
| INTERNAL_WISE | 1944 | 1 | -22 500,00 |
| OWNER_LOAN_2893 | 2893 | 6 | 19 004,19 |
| MARKETING_NO_VAT | 5900 | 3 | 18 600,00 |
| PRIVATE_FOOD | — | 7 | -5 108,50 |
| INTEREST | 8400 | 7 | -3 722,21 |
| HOTEL | 5810 | 3 | -3 593,34 |
| IT_HOSTING | 6540 | 2 | -1 783,75 |
| PRIVATE_KLARNA | 2893 | 2 | -1 326,86 |
| TRAVEL_DOMESTIC | 5810 | 6 | -1 011,00 |
| SOFTWARE_NO_VAT | 5420 | 11 | -938,82 |
| MOBILE_SUBSCRIPTION | 6212 | 12 | -915,74 |
| BANK_FEE | 6570 | 7 | -280,00 |
| SUPPLIES | 5460 | 1 | -259,80 |
| INTEREST_INCOME | 8311 | 2 | 16,25 |
| OWNER_PRIVATE_2893 | 2893 | 69 | 12,65 |

## 4. Sammanställning per BAS-konto (motkonto)

| Konto | Namn | Antal | Summa SEK |
|---|---|---:|---:|
| 3051 | Försäljning Shopify/Swish 25% | 21 | 40 020,00 |
| 1910 |  | 15 | -31 500,00 |
| 1944 | Wise EUR | 1 | -22 500,00 |
| 5900 |  | 3 | 18 600,00 |
| 2893 | Skuld till närstående (Sami) | 77 | 17 689,98 |
| — |  | 7 | -5 108,50 |
| 5810 | Resor | 9 | -4 604,34 |
| 8400 |  | 7 | -3 722,21 |
| 6540 |  | 2 | -1 783,75 |
| 5420 |  | 11 | -938,82 |
| 6212 | Mobiltelefon | 12 | -915,74 |
| 6570 | Bankkostnader | 7 | -280,00 |
| 5460 | Förbrukningsmaterial | 1 | -259,80 |
| 8311 |  | 2 | 16,25 |

## 5. Alla 175 transaktioner (kronologiskt)

Markera rader med ⚠️ → behöver din bekräftelse innan SE-fil byggs.

| # | Datum | SEK | Original | R | Konto | Kategori | Motpart / Beskrivning | Anledning | ⚠️ |
|---:|---|---:|---:|:---:|:---:|---|---|---|:---:|
| 1 | 2026-01-02 | -20.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA* 0735165708 AVG | Privat konto - måste vara tydligt företagsre… |  |
| 2 | 2026-01-02 | -60.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA* 0735147846 AVG | Privat konto - måste vara tydligt företagsre… |  |
| 3 | 2026-01-02 | -60.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA* 0735299675 AVG | Privat konto - måste vara tydligt företagsre… |  |
| 4 | 2026-01-02 | -60.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA* 0793392306 AVG | Privat konto - måste vara tydligt företagsre… |  |
| 5 | 2026-01-03 | 3000.00 |  | I | 3051 | SALES | Swish inbetalning Khazare Aldeen | Privat konto - måste vara tydligt företagsre… |  |
| 6 | 2026-01-05 | -430.60 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 7 | 2026-01-05 | -891.21 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 8 | 2026-01-07 | -650.00 |  | O | 2893 | OWNER_PRIVATE_2893 | LAGER 157 ESKIL | Privat konto - måste vara tydligt företagsre… |  |
| 9 | 2026-01-07 | -464.85 |  | O | 2893 | OWNER_PRIVATE_2893 | CITY GROSS ESKILSTUN | Privat konto - måste vara tydligt företagsre… |  |
| 10 | 2026-01-07 | -117.00 |  | O | 2893 | OWNER_PRIVATE_2893 | ESKILSTUNA HALAL KOTT | Privat konto - måste vara tydligt företagsre… |  |
| 11 | 2026-01-07 | -39.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 12 | 2026-01-07 | -2600.00 |  | O | 2893 | OWNER_PRIVATE_2893 | 92356405879 | Privat konto - måste vara tydligt företagsre… |  |
| 13 | 2026-01-07 | 1700.00 |  | I | 3051 | SALES | Swish inbetalning JARAH ALAHMAD | Privat konto - måste vara tydligt företagsre… |  |
| 14 | 2026-01-08 | -2477.92 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260106 MONEYGRAM GREECE | Privat konto - måste vara tydligt företagsre… |  |
| 15 | 2026-01-11 | -249.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 16 | 2026-01-12 | -254.58 |  | O | 2893 | OWNER_PRIVATE_2893 | MATNARA FROSLUNDA | Privat konto - måste vara tydligt företagsre… |  |
| 17 | 2026-01-16 | -18.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 18 | 2026-01-16 | -1.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 19 | 2026-01-18 | -39.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 20 | 2026-01-18 | 200.00 |  | I | 3051 | SALES | Swish inbetalning PERSONUPPGIFT SKY | Privat konto - måste vara tydligt företagsre… |  |
| 21 | 2026-01-19 | 200.00 |  | I | 3051 | SALES | Swish inbetalning SAFAA ALGHARIB | Privat konto - måste vara tydligt företagsre… |  |
| 22 | 2026-01-20 | -1500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 23 | 2026-01-20 | 1325.00 |  | I | 2893 | OWNER_PRIVATE_2893 | BARNBDR 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 24 | 2026-01-22 | 1500.00 |  | I | 3051 | SALES | Swish inbetalning NOURA YASSIN ALFA | Privat konto - måste vara tydligt företagsre… |  |
| 25 | 2026-01-22 | 4000.00 |  | I | 3051 | SALES | Swish inbetalning KOLISTAN HAMO | Privat konto - måste vara tydligt företagsre… |  |
| 26 | 2026-01-22 | 0.14 |  | I | 2893 | OWNER_PRIVATE_2893 | MARGINALEN 92356421890 | Privat konto - måste vara tydligt företagsre… |  |
| 27 | 2026-01-22 | -1197.78 |  | O | 5810 | HOTEL | Autogiro K*Booking.co | Privat konto - måste vara tydligt företagsre… |  |
| 28 | 2026-01-22 | 18910.00 |  | I | 2893 | OWNER_PRIVATE_2893 | Studiestöd | Privat konto - måste vara tydligt företagsre… |  |
| 29 | 2026-01-23 | 770.00 |  | I | 3051 | SALES | Swish inbetalning MANAL DAHAM DAKLA | Privat konto - måste vara tydligt företagsre… |  |
| 30 | 2026-01-23 | -22500.00 |  | O | 1944 | INTERNAL_WISE | Betalning BG 5525-0500 WISE EUROPE | Privat konto - måste vara tydligt företagsre… |  |
| 31 | 2026-01-23 | 7564.00 |  | I | 2893 | OWNER_PRIVATE_2893 | Studiestöd | Privat konto - måste vara tydligt företagsre… |  |
| 32 | 2026-01-24 | -99.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 33 | 2026-01-24 | -99.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 34 | 2026-01-24 | -129.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 35 | 2026-01-26 | -297.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 36 | 2026-01-26 | -294.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 37 | 2026-01-26 | 1100.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 38 | 2026-01-26 | 5000.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 39 | 2026-01-26 | 1450.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 40 | 2026-01-27 | 3000.00 |  | I | 2893 | OWNER_LOAN_2893 | Insättning 92356405879 | Privat konto - måste vara tydligt företagsre… |  |
| 41 | 2026-01-27 | -900.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking PG 4846800-3 ESKILSTUN | Privat konto - måste vara tydligt företagsre… |  |
| 42 | 2026-01-27 | -800.00 |  | O | — | PRIVATE_FOOD | Betalning BG 5127-5477 American Exp | Privat konto - måste vara tydligt företagsre… |  |
| 43 | 2026-01-27 | -1610.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning BG 319-9973 Hi3G Access A | Privat konto - måste vara tydligt företagsre… |  |
| 44 | 2026-01-27 | -1197.78 |  | O | 5810 | HOTEL | Autogiro K*Booking.co | Privat konto - måste vara tydligt företagsre… |  |
| 45 | 2026-01-27 | -99.00 |  | O | 2893 | PRIVATE_KLARNA | Autogiro K*G&S | Privat konto - måste vara tydligt företagsre… |  |
| 46 | 2026-01-27 | 6200.00 |  | I | 5900 | MARKETING_NO_VAT | BOSTADSB 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 47 | 2026-01-28 | 2500.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 48 | 2026-01-28 | -461.00 |  | O | 2893 | OWNER_PRIVATE_2893 | ADAM KOTT | Privat konto - måste vara tydligt företagsre… |  |
| 49 | 2026-01-28 | 3500.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 50 | 2026-01-28 | -79.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 51 | 2026-01-28 | -2500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4187600-4 Nordea Gold | Privat konto - måste vara tydligt företagsre… |  |
| 52 | 2026-01-28 | 2740.00 |  | I | 2893 | OWNER_LOAN_2893 | 2893 | Privat konto - måste vara tydligt företagsre… |  |
| 53 | 2026-01-28 | -3500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4173300-7 Nordea Premi | Privat konto - måste vara tydligt företagsre… |  |
| 54 | 2026-01-28 | -15239.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking BG 305-6520 VICTORIA P | Privat konto - måste vara tydligt företagsre… |  |
| 55 | 2026-01-29 | -1000.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 56 | 2026-01-30 | -79.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning Samis Jackets AB | Privat konto - måste vara tydligt företagsre… |  |
| 57 | 2026-01-31 | 2.34 |  | I | 8311 | INTEREST_INCOME | Nordea Cashback | Privat konto - måste vara tydligt företagsre… |  |
| 58 | 2026-02-05 | -402.76 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 59 | 2026-02-05 | -0.90 |  | O | 8400 | INTEREST | DRÖJSMÅLSRÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 60 | 2026-02-05 | -860.62 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 61 | 2026-02-07 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 62 | 2026-02-07 | -1000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 63 | 2026-02-09 | 200.00 |  | I | 3051 | SALES | Swish inbetalning IKHLAS MOHAMAD | Privat konto - måste vara tydligt företagsre… |  |
| 64 | 2026-02-11 | -249.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 65 | 2026-02-13 | -383.00 |  | O | 5810 | TRAVEL_DOMESTIC | Swish betalning MÄLARDALSTRAFIK AKT | Privat konto - måste vara tydligt företagsre… |  |
| 66 | 2026-02-13 | -134.80 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260212 ARAN FOOD AB | Privat konto - måste vara tydligt företagsre… |  |
| 67 | 2026-02-15 | -180.00 |  | O | 2893 | OWNER_PRIVATE_2893 | ADAM KOTT | Privat konto - måste vara tydligt företagsre… |  |
| 68 | 2026-02-16 | -18.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 69 | 2026-02-16 | 2.50 |  | I | 2893 | OWNER_PRIVATE_2893 | Swish återbetalning EASYPARK AB | Privat konto - måste vara tydligt företagsre… |  |
| 70 | 2026-02-16 | -15.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning EASYPARK AB | Privat konto - måste vara tydligt företagsre… |  |
| 71 | 2026-02-17 | 8222.99 |  | I | 2893 | OWNER_LOAN_2893 | Utlandsinsättning 5420723 | Privat konto - måste vara tydligt företagsre… |  |
| 72 | 2026-02-17 | 210.06 |  | I | 2893 | OWNER_LOAN_2893 | Utlandsinsättning 5402275 | Privat konto - måste vara tydligt företagsre… |  |
| 73 | 2026-02-18 | -39.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 74 | 2026-02-18 | -4000.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning PATRIK HALLBÄCK | Privat konto - måste vara tydligt företagsre… |  |
| 75 | 2026-02-18 | 1000.00 |  | I | 3051 | SALES | Swish inbetalning GEORGE HAILI | Privat konto - måste vara tydligt företagsre… |  |
| 76 | 2026-02-18 | 2000.00 |  | I | 3051 | SALES | Swish inbetalning GEORGE HAILI | Privat konto - måste vara tydligt företagsre… |  |
| 77 | 2026-02-18 | -312.30 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260217 METRO SUPERMARKET AB | Privat konto - måste vara tydligt företagsre… |  |
| 78 | 2026-02-18 | -5000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260217 ATM MAXI ICA ST | Privat konto - måste vara tydligt företagsre… |  |
| 79 | 2026-02-19 | -372.60 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260218 ARAN FOOD AB | Privat konto - måste vara tydligt företagsre… |  |
| 80 | 2026-02-20 | -29.90 |  | O | — | PRIVATE_FOOD | WILLYS ESKILSTUNA C | Privat konto - måste vara tydligt företagsre… |  |
| 81 | 2026-02-20 | -102.85 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735147846 FEB | Privat konto - måste vara tydligt företagsre… |  |
| 82 | 2026-02-20 | -60.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0793392306 FEB | Privat konto - måste vara tydligt företagsre… |  |
| 83 | 2026-02-20 | -60.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735299675 FEB | Privat konto - måste vara tydligt företagsre… |  |
| 84 | 2026-02-20 | -20.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735165708 FEB | Privat konto - måste vara tydligt företagsre… |  |
| 85 | 2026-02-20 | 400.00 |  | I | 3051 | SALES | Swish inbetalning TAREK ZAKARIA FAW | Privat konto - måste vara tydligt företagsre… |  |
| 86 | 2026-02-20 | 1325.00 |  | I | 2893 | OWNER_PRIVATE_2893 | BARNBDR 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 87 | 2026-02-21 | -92.94 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260220 ARAN FOOD AB | Privat konto - måste vara tydligt företagsre… |  |
| 88 | 2026-02-23 | -700.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260222 ESKILSTUNA HALAL KOT | Privat konto - måste vara tydligt företagsre… |  |
| 89 | 2026-02-23 | -293.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 90 | 2026-02-23 | -292.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 91 | 2026-02-23 | -260.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4950302-2 REGION SÖRML | Privat konto - måste vara tydligt företagsre… |  |
| 92 | 2026-02-23 | -1610.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning BG 319-9973 Hi3G Access A | Privat konto - måste vara tydligt företagsre… |  |
| 93 | 2026-02-24 | 20000.00 |  | I | 2893 | OWNER_PRIVATE_2893 | ÅTERBET LÅN 92356405879 | Privat konto - måste vara tydligt företagsre… |  |
| 94 | 2026-02-25 | 11000.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 95 | 2026-02-25 | -11000.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4173300-7 Nordea Premi | Privat konto - måste vara tydligt företagsre… |  |
| 96 | 2026-02-25 | -1131.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking PG 4846800-3 ESKILSTUN | Privat konto - måste vara tydligt företagsre… |  |
| 97 | 2026-02-25 | -15239.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking BG 305-6520 VICTORIA P | Privat konto - måste vara tydligt företagsre… |  |
| 98 | 2026-02-25 | 15128.00 |  | I | 2893 | OWNER_PRIVATE_2893 | Studiestöd | Privat konto - måste vara tydligt företagsre… |  |
| 99 | 2026-02-26 | -800.00 |  | O | — | PRIVATE_FOOD | Betalning BG 5127-5477 American Exp | Privat konto - måste vara tydligt företagsre… |  |
| 100 | 2026-02-27 | -1073.70 |  | O | — | PRIVATE_FOOD | WILLYS ESKILSTUNA C | Privat konto - måste vara tydligt företagsre… |  |
| 101 | 2026-02-27 | 4500.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 102 | 2026-02-27 | -3000.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning HANNA JOKHAJI | Privat konto - måste vara tydligt företagsre… |  |
| 103 | 2026-02-27 | -4500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4187600-4 Nordea Gold | Privat konto - måste vara tydligt företagsre… |  |
| 104 | 2026-02-27 | 6200.00 |  | I | 5900 | MARKETING_NO_VAT | BOSTADSB 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 105 | 2026-02-28 | -2983.75 |  | O | 6540 | IT_HOSTING | One.com | Privat konto - måste vara tydligt företagsre… |  |
| 106 | 2026-03-02 | -116.77 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735165708 MARS | Privat konto - måste vara tydligt företagsre… |  |
| 107 | 2026-03-02 | -120.00 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735147846 MARS | Privat konto - måste vara tydligt företagsre… |  |
| 108 | 2026-03-02 | -118.06 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0793392306 MARS | Privat konto - måste vara tydligt företagsre… |  |
| 109 | 2026-03-02 | -118.06 |  | O | 6212 | MOBILE_SUBSCRIPTION | VIMLA 0735299675 MARS | Privat konto - måste vara tydligt företagsre… |  |
| 110 | 2026-03-02 | -800.00 |  | O | — | PRIVATE_FOOD | Betalning BG 5127-5477 American Exp | Privat konto - måste vara tydligt företagsre… |  |
| 111 | 2026-03-03 | -383.00 |  | O | 5810 | TRAVEL_DOMESTIC | Swish betalning MÄLARDALSTRAFIK AKT | Privat konto - måste vara tydligt företagsre… |  |
| 112 | 2026-03-04 | -875.90 |  | O | — | PRIVATE_FOOD | Kortköp 260303 WILLYS ESKILSTUNA C | Privat konto - måste vara tydligt företagsre… |  |
| 113 | 2026-03-04 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260303 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 114 | 2026-03-05 | -70.00 |  | O | 5810 | TRAVEL_DOMESTIC | SORMLANDSTRAFIKEN | Privat konto - måste vara tydligt företagsre… |  |
| 115 | 2026-03-05 | -369.13 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 116 | 2026-03-05 | -766.99 |  | O | 8400 | INTEREST | RÖRLIG RÄNTA | Privat konto - måste vara tydligt företagsre… |  |
| 117 | 2026-03-05 | -800.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 118 | 2026-03-06 | -70.00 |  | O | 5810 | TRAVEL_DOMESTIC | SORMLANDSTRAFIKEN | Privat konto - måste vara tydligt företagsre… |  |
| 119 | 2026-03-07 | -35.00 |  | O | 5810 | TRAVEL_DOMESTIC | SORMLANDSTRAFIKEN | Privat konto - måste vara tydligt företagsre… |  |
| 120 | 2026-03-07 | 18.18 |  | I | 5420 | SOFTWARE_NO_VAT | GOOGLE *ADS5215017274 | Privat konto - måste vara tydligt företagsre… |  |
| 121 | 2026-03-09 | 1200.00 |  | I | 6540 | IT_HOSTING | One.com | Privat konto - måste vara tydligt företagsre… |  |
| 122 | 2026-03-09 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 123 | 2026-03-09 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 124 | 2026-03-09 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 125 | 2026-03-09 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 126 | 2026-03-09 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 127 | 2026-03-09 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 128 | 2026-03-09 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 129 | 2026-03-09 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 130 | 2026-03-09 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 131 | 2026-03-09 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 132 | 2026-03-09 | -500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning BASHAR RAED HAMOUD | Privat konto - måste vara tydligt företagsre… |  |
| 133 | 2026-03-09 | 10631.14 |  | I | 2893 | OWNER_LOAN_2893 | Insättning | Privat konto - måste vara tydligt företagsre… |  |
| 134 | 2026-03-10 | -40.00 |  | O | 6570 | BANK_FEE | KONTANTUTTAGSAVGIFT | Privat konto - måste vara tydligt företagsre… |  |
| 135 | 2026-03-10 | -200.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Jafaris Group AB 201 | Privat konto - måste vara tydligt företagsre… |  |
| 136 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | ATM KONTANTEN 4167 CIT | Privat konto - måste vara tydligt företagsre… |  |
| 137 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260309 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 138 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260309 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 139 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260309 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 140 | 2026-03-10 | -1500.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260310 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 141 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260309 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 142 | 2026-03-10 | -2000.00 |  | O | 1910 | CASH_WITHDRAWAL | Kontantuttag 260309 ATM KONTANTEN 4 | Privat konto - måste vara tydligt företagsre… |  |
| 143 | 2026-03-11 | -259.80 |  | O | 5460 | SUPPLIES | CLAS OHLSON | Privat konto - måste vara tydligt företagsre… |  |
| 144 | 2026-03-11 | -70.00 |  | O | 5810 | TRAVEL_DOMESTIC | SORMLANDSTRAFIKEN | Privat konto - måste vara tydligt företagsre… |  |
| 145 | 2026-03-11 | -249.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 146 | 2026-03-13 | -729.00 |  | O | — | PRIVATE_FOOD | WILLYS ESKILSTUNA C | Privat konto - måste vara tydligt företagsre… |  |
| 147 | 2026-03-13 | -200.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning BASHAR RAED HAMOUD | Privat konto - måste vara tydligt företagsre… |  |
| 148 | 2026-03-16 | -18.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 149 | 2026-03-18 | -39.00 |  | O | 5420 | SOFTWARE_NO_VAT | APPLE.COM/BILL | Privat konto - måste vara tydligt företagsre… |  |
| 150 | 2026-03-19 | 2000.00 |  | I | 3051 | SALES | Swish inbetalning TOREKI MARASH | Privat konto - måste vara tydligt företagsre… |  |
| 151 | 2026-03-20 | 1325.00 |  | I | 2893 | OWNER_PRIVATE_2893 | BARNBDR 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 152 | 2026-03-23 | 1800.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 153 | 2026-03-24 | -2595.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Kortköp 260323 SPECSAVERS OPTIK | Privat konto - måste vara tydligt företagsre… |  |
| 154 | 2026-03-24 | -1197.78 |  | O | 5810 | HOTEL | Autogiro K*Booking.co | Privat konto - måste vara tydligt företagsre… |  |
| 155 | 2026-03-25 | 3000.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 156 | 2026-03-25 | 5500.00 |  | I | 2893 | OWNER_PRIVATE_2893 | INBETALNING | Privat konto - måste vara tydligt företagsre… |  |
| 157 | 2026-03-25 | -3000.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4187600-4 Nordea Gold | Privat konto - måste vara tydligt företagsre… |  |
| 158 | 2026-03-25 | -5500.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4173300-7 Nordea Premi | Privat konto - måste vara tydligt företagsre… |  |
| 159 | 2026-03-25 | -1600.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning PG 4187500-6 BANK NORWEGI | Privat konto - måste vara tydligt företagsre… |  |
| 160 | 2026-03-25 | -260.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 161 | 2026-03-25 | -289.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 162 | 2026-03-25 | -293.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Swish betalning ENTERCARD GROUP AB | Privat konto - måste vara tydligt företagsre… |  |
| 163 | 2026-03-25 | 15128.00 |  | I | 2893 | OWNER_PRIVATE_2893 | Studiestöd | Privat konto - måste vara tydligt företagsre… |  |
| 164 | 2026-03-26 | 1500.00 |  | I | 3051 | SALES | Swish inbetalning ALMA ALSKAA | Privat konto - måste vara tydligt företagsre… |  |
| 165 | 2026-03-26 | 7000.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 166 | 2026-03-26 | 4800.00 |  | I | 3051 | SALES | Swish inbetalning ALNABLSI,JOMANA | Privat konto - måste vara tydligt företagsre… |  |
| 167 | 2026-03-26 | -1125.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking PG 4846800-3 ESKILSTUN | Privat konto - måste vara tydligt företagsre… |  |
| 168 | 2026-03-26 | -1610.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Betalning BG 319-9973 Hi3G Access A | Privat konto - måste vara tydligt företagsre… |  |
| 169 | 2026-03-27 | -5800.00 |  | O | 2893 | OWNER_LOAN_2893 | From 2893 9235 64 05879 | Privat konto - måste vara tydligt företagsre… |  |
| 170 | 2026-03-27 | -15239.00 |  | O | 2893 | OWNER_PRIVATE_2893 | Open Banking BG 305-6520 VICTORIA P | Privat konto - måste vara tydligt företagsre… |  |
| 171 | 2026-03-27 | -1227.86 |  | O | 2893 | PRIVATE_KLARNA | Autogiro K* Klarna | Privat konto - måste vara tydligt företagsre… |  |
| 172 | 2026-03-27 | 6200.00 |  | I | 5900 | MARKETING_NO_VAT | BOSTADSB 1986021750700484 | Privat konto - måste vara tydligt företagsre… |  |
| 173 | 2026-03-30 | 200.00 |  | I | 3051 | SALES | Swish inbetalning PERSONUPPGIFT SKY | Privat konto - måste vara tydligt företagsre… |  |
| 174 | 2026-03-31 | 13.91 |  | I | 8311 | INTEREST_INCOME | Nordea Cashback | Privat konto - måste vara tydligt företagsre… |  |
| 175 | 2026-03-31 | 200.00 |  | I | 3051 | SALES | Swish inbetalning SHIYAN ALLAH WERD | Privat konto - måste vara tydligt företagsre… |  |

---
_Genererad av `build_per_bank_audit.py` från `AUDIT_Q1_2026_FILL_REASONS.csv`._