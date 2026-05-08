# 📂 Lunar Bank — Audit Q1 2026 (Samis Jackets AB)

**Period:** 2026-01-01 → 2026-03-31  |  **Genererad:** 2026-04-29
**Föreslaget bankkonto:** 1948 (Lunar Bank)

## 1. Källfiler i denna mapp

Följande råfiler från banken låg i denna mapp och bearbetades av `build_audit_csv.py`. Räkna gärna manuellt i CSV:erna och jämför kolumnen *Rader i råfilen* mot *Inlästa transaktioner*.

| Råfil | Rader i råfilen (datalinjer) | Inlästa transaktioner |
|---|---:|---:|
| AUDIT_Lunar_Bank_Q1_2026.csv | 273 | 0 ⚠️ (kontrollera) |
| Lunar export.csv | 273 | 273 ✅ |
| **TOTALT** | — | **273** |

> ⚠️ Skillnad i antal raden kan bero på filtrering av rubrik-/summarader. Alla rubrik-/summarader hoppas över medvetet.

## 2. Kontrolltotaler

- **IN (insättningar):** 95 464,31 SEK
- **UT (uttag):** -87 719,83 SEK
- **Netto perioden:** 7 744,48 SEK
- **Antal needs_review:** 0

## 3. Sammanställning per kategori

| Kategori | Konto(n) | Antal | Summa SEK |
|---|---|---:|---:|
| SALES | 3051 | 123 | 94 978,31 |
| INTERNAL_TRANSFER | 1930 | 7 | -77 864,00 |
| FREIGHT | 5700 | 1 | -3 463,00 |
| OWNER_LOAN_2893 | 2893 | 7 | -2 254,00 |
| SALES_REFUND | 3051 | 3 | -1 870,00 |
| BANK_FEE | 6570 | 131 | -1 494,97 |
| IT_SERVICES_NO_VAT | 6540 | 1 | -287,86 |

## 4. Sammanställning per BAS-konto (motkonto)

| Konto | Namn | Antal | Summa SEK |
|---|---|---:|---:|
| 3051 | Försäljning Shopify/Swish 25% | 126 | 93 108,31 |
| 1930 | Marginalen företagskonto | 7 | -77 864,00 |
| 5700 |  | 1 | -3 463,00 |
| 2893 | Skuld till närstående (Sami) | 7 | -2 254,00 |
| 6570 | Bankkostnader | 131 | -1 494,97 |
| 6540 |  | 1 | -287,86 |

## 5. Alla 273 transaktioner (kronologiskt)

Markera rader med ⚠️ → behöver din bekräftelse innan SE-fil byggs.

| # | Datum | SEK | Original | R | Konto | Kategori | Motpart / Beskrivning | Anledning | ⚠️ |
|---:|---|---:|---:|:---:|:---:|---|---|---|:---:|
| 1 | 2026-01-16 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 2 | 2026-01-16 | 375.00 |  | I | 3051 | SALES | MAROUKEL, NANCY |  |  |
| 3 | 2026-01-16 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 4 | 2026-01-16 | 1.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 5 | 2026-01-16 | -37.74 |  | O | 6570 | BANK_FEE | Swish Business enrollment |  |  |
| 6 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 7 | 2026-01-17 | 299.00 |  | I | 3051 | SALES | RASHA AL-SAFFAR |  |  |
| 8 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 9 | 2026-01-17 | 1179.00 |  | I | 3051 | SALES | RASHA AL-SAFFAR |  |  |
| 10 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 11 | 2026-01-17 | 4480.00 |  | I | 3051 | SALES | ELAF ALAMIN |  |  |
| 12 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 13 | 2026-01-17 | 900.00 |  | I | 3051 | SALES | ABDUL BASET ALSALAMA |  |  |
| 14 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 15 | 2026-01-17 | 200.00 |  | I | 3051 | SALES | ABDUL BASET ALSALAMA |  |  |
| 16 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 17 | 2026-01-17 | 1379.00 |  | I | 3051 | SALES | ABEER SALIM |  |  |
| 18 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 19 | 2026-01-17 | 200.00 |  | I | 3051 | SALES | RASHA AL-SAFFAR |  |  |
| 20 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 21 | 2026-01-17 | 200.00 |  | I | 3051 | SALES | ABEER SALIM |  |  |
| 22 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 23 | 2026-01-17 | 200.00 |  | I | 3051 | SALES | REEM SHAYAH |  |  |
| 24 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 25 | 2026-01-17 | 1579.00 |  | I | 3051 | SALES | SHEIKH HUSSEIN,BUSHRA |  |  |
| 26 | 2026-01-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 27 | 2026-01-17 | 200.00 |  | I | 3051 | SALES | OSSMAN,ROQEIA |  |  |
| 28 | 2026-01-18 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 29 | 2026-01-18 | 200.00 |  | I | 3051 | SALES | JUBRAN JOMEH YASSIN ABBASI |  |  |
| 30 | 2026-01-18 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 31 | 2026-01-18 | 1100.00 |  | I | 3051 | SALES | OSSMAN,ROQEIA |  |  |
| 32 | 2026-01-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 33 | 2026-01-19 | 200.00 |  | I | 3051 | SALES | AL MOHAMMAD ALHADI,NIRAN |  |  |
| 34 | 2026-01-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 35 | 2026-01-19 | 1079.00 |  | I | 3051 | SALES | SAFAA ALGHARIB |  |  |
| 36 | 2026-01-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 37 | 2026-01-19 | 1080.00 |  | I | 3051 | SALES | MAYADA JUMAA |  |  |
| 38 | 2026-01-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 39 | 2026-01-19 | 200.00 |  | I | 3051 | SALES | MAYADA JUMAA |  |  |
| 40 | 2026-01-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 41 | 2026-01-20 | 200.00 |  | I | 3051 | SALES | DONIA TKHOMI |  |  |
| 42 | 2026-01-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 43 | 2026-01-20 | 1000.00 |  | I | 3051 | SALES | SHEIKH HUSSEIN,BUSHRA |  |  |
| 44 | 2026-01-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 45 | 2026-01-20 | 79.00 |  | I | 3051 | SALES | NOUR AKHRAS |  |  |
| 46 | 2026-01-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 47 | 2026-01-20 | 1079.00 |  | I | 3051 | SALES | ALELAWI,BOTOUL |  |  |
| 48 | 2026-01-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 49 | 2026-01-20 | 779.00 |  | I | 3051 | SALES | ALMA ALSKAA |  |  |
| 50 | 2026-01-21 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 51 | 2026-01-21 | 1100.00 |  | I | 3051 | SALES | DONIA TKHOMI |  |  |
| 52 | 2026-01-21 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 53 | 2026-01-21 | 1079.00 |  | I | 3051 | SALES | HANAN ALDAABOUL |  |  |
| 54 | 2026-01-21 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 55 | 2026-01-21 | 200.00 |  | I | 3051 | SALES | HANAN ALDAABOUL |  |  |
| 56 | 2026-01-22 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 57 | 2026-01-22 | 1279.00 |  | I | 3051 | SALES | ESSRAA MOHAMMED AHMED |  |  |
| 58 | 2026-01-22 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 59 | 2026-01-22 | 500.00 |  | I | 3051 | SALES | HASANHOSIN, EEAD |  |  |
| 60 | 2026-01-22 | -1190.00 |  | O | 6570 | BANK_FEE | Lunar Plan Essential |  |  |
| 61 | 2026-01-22 | -20489.00 |  | O | 1930 | INTERNAL_TRANSFER | Swish sales | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 62 | 2026-01-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 63 | 2026-01-23 | 379.00 |  | I | 3051 | SALES | ALSABBAGH,ALAA |  |  |
| 64 | 2026-01-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 65 | 2026-01-24 | 99.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 66 | 2026-01-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 67 | 2026-01-24 | 99.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 68 | 2026-01-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 69 | 2026-01-24 | 129.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 70 | 2026-01-25 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 71 | 2026-01-25 | 79.00 |  | I | 3051 | SALES | PERSONUPPGIFT SKYDDAD |  |  |
| 72 | 2026-01-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 73 | 2026-01-26 | 1080.00 |  | I | 3051 | SALES | NOUR ABDEEN |  |  |
| 74 | 2026-01-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 75 | 2026-01-27 | 429.00 |  | I | 3051 | SALES | RAEDA SOBH |  |  |
| 76 | 2026-01-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 77 | 2026-01-27 | 1750.00 |  | I | 3051 | SALES | ELAF ALAMIN |  |  |
| 78 | 2026-01-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 79 | 2026-01-27 | 300.00 |  | I | 3051 | SALES | AWADYA SALEH |  |  |
| 80 | 2026-01-28 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 81 | 2026-01-28 | 79.00 |  | I | 3051 | SALES | PERSONUPPGIFT SKYDDAD |  |  |
| 82 | 2026-01-28 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 83 | 2026-01-28 | 79.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 84 | 2026-01-28 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 85 | 2026-01-28 | 250.00 |  | I | 3051 | SALES | ATAA MAHMOUD HMEDAN |  |  |
| 86 | 2026-01-28 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 87 | 2026-01-28 | 1279.00 |  | I | 3051 | SALES | MOHAMMAD ALNAEF |  |  |
| 88 | 2026-01-28 | -429.00 |  | O | 3051 | SALES_REFUND | Retur refund Sweish | Kund-namn på Lunar OUT = återbetalning av fö… |  |
| 89 | 2026-01-28 | -2740.00 |  | O | 2893 | OWNER_LOAN_2893 | 2893 återbetalning |  |  |
| 90 | 2026-01-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 91 | 2026-01-29 | 459.00 |  | I | 3051 | SALES | NAJMA DAYIB |  |  |
| 92 | 2026-01-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 93 | 2026-01-29 | 200.00 |  | I | 3051 | SALES | ABOUD,MARYAM |  |  |
| 94 | 2026-01-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 95 | 2026-01-29 | 329.00 |  | I | 3051 | SALES | FATIMA ASAAD |  |  |
| 96 | 2026-01-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 97 | 2026-01-30 | 79.00 |  | I | 2893 | OWNER_LOAN_2893 | ALSHAREF,MOHAMMAD SAMI |  |  |
| 98 | 2026-01-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 99 | 2026-01-30 | 932.00 |  | I | 3051 | SALES | ASMAA SABBAGH |  |  |
| 100 | 2026-01-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 101 | 2026-01-31 | 429.00 |  | I | 3051 | SALES | AWADYA SALEH |  |  |
| 102 | 2026-02-02 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 103 | 2026-02-02 | 340.00 |  | I | 3051 | SALES | Assaf Ali Alkasoum |  |  |
| 104 | 2026-02-02 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 105 | 2026-02-02 | 415.00 |  | I | 3051 | SALES | ALMA ALSKAA |  |  |
| 106 | 2026-02-02 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 107 | 2026-02-02 | 1078.00 |  | I | 3051 | SALES | Assaf Ali Alkasoum |  |  |
| 108 | 2026-02-03 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 109 | 2026-02-03 | 510.00 |  | I | 3051 | SALES | MOHAMMAD ALNAEF |  |  |
| 110 | 2026-02-03 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 111 | 2026-02-03 | 1350.00 |  | I | 3051 | SALES | EBRAHIM,NEAMAT ALI ADAM |  |  |
| 112 | 2026-02-03 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 113 | 2026-02-03 | 1350.00 |  | I | 3051 | SALES | MAYADA JUMAA |  |  |
| 114 | 2026-02-03 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 115 | 2026-02-03 | 800.00 |  | I | 3051 | SALES | PERSONUPPGIFT SKYDDAD |  |  |
| 116 | 2026-02-04 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 117 | 2026-02-04 | 350.00 |  | I | 3051 | SALES | SHADI ALMOUSA ALAHMAD |  |  |
| 118 | 2026-02-04 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 119 | 2026-02-04 | 79.00 |  | I | 3051 | SALES | ASMAA SABBAGH |  |  |
| 120 | 2026-02-04 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 121 | 2026-02-04 | 1000.00 |  | I | 3051 | SALES | KHALED ALMOHAMMAD |  |  |
| 122 | 2026-02-06 | -13104.00 |  | O | 1930 | INTERNAL_TRANSFER | Transfer | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 123 | 2026-02-08 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 124 | 2026-02-08 | 2200.00 |  | I | 3051 | SALES | GHENA JARKAS |  |  |
| 125 | 2026-02-08 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 126 | 2026-02-08 | 1000.00 |  | I | 3051 | SALES | ABDULMASIH BLÜME, NAHLA |  |  |
| 127 | 2026-02-08 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 128 | 2026-02-08 | 1800.00 |  | I | 3051 | SALES | ABDULMASIH BLÜME, NAHLA |  |  |
| 129 | 2026-02-08 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 130 | 2026-02-08 | 200.00 |  | I | 3051 | SALES | GHENA JARKAS |  |  |
| 131 | 2026-02-08 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 132 | 2026-02-08 | 350.00 |  | I | 3051 | SALES | ABDULMASIH BLÜME, NAHLA |  |  |
| 133 | 2026-02-09 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 134 | 2026-02-09 | 1430.00 |  | I | 3051 | SALES | IKHLAS MOHAMAD |  |  |
| 135 | 2026-02-09 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 136 | 2026-02-09 | 79.00 |  | I | 3051 | SALES | PERSONUPPGIFT SKYDDAD |  |  |
| 137 | 2026-02-09 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 138 | 2026-02-09 | 200.00 |  | I | 3051 | SALES | ALTAMARI, MONA |  |  |
| 139 | 2026-02-09 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 140 | 2026-02-09 | 258.00 |  | I | 3051 | SALES | AL KHALED,HANAA |  |  |
| 141 | 2026-02-10 | -7500.00 |  | O | 1930 | INTERNAL_TRANSFER | Transfer | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 142 | 2026-02-11 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 143 | 2026-02-11 | 379.00 |  | I | 3051 | SALES | RAUDH FOIED |  |  |
| 144 | 2026-02-11 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 145 | 2026-02-11 | 280.00 |  | I | 3051 | SALES | PERSONUPPGIFT SKYDDAD |  |  |
| 146 | 2026-02-11 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 147 | 2026-02-11 | 200.00 |  | I | 3051 | SALES | Personuppgift skyddad |  |  |
| 148 | 2026-02-11 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 149 | 2026-02-11 | 200.00 |  | I | 3051 | SALES | RAUDH FOIED |  |  |
| 150 | 2026-02-15 | -39.00 |  | O | 6570 | BANK_FEE | Swish Business enrollment |  |  |
| 151 | 2026-02-17 | -221.00 |  | O | 3051 | SALES_REFUND | Najma Dayib | Kund-namn på Lunar OUT = återbetalning av fö… |  |
| 152 | 2026-02-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 153 | 2026-02-20 | 1000.00 |  | I | 3051 | SALES | ALAMIN,AMNA MOHAMMEDALI |  |  |
| 154 | 2026-02-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 155 | 2026-02-20 | 1087.00 |  | I | 3051 | SALES | AWADYA SALEH |  |  |
| 156 | 2026-02-22 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 157 | 2026-02-22 | 1300.00 |  | I | 3051 | SALES | YOUSRA DALATI |  |  |
| 158 | 2026-02-22 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 159 | 2026-02-22 | 1500.00 |  | I | 3051 | SALES | ABDULMASIH BLÜME, NAHLA |  |  |
| 160 | 2026-02-22 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 161 | 2026-02-22 | 200.00 |  | I | 3051 | SALES | YOUSRA DALATI |  |  |
| 162 | 2026-02-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 163 | 2026-02-23 | 1237.00 |  | I | 3051 | SALES | AYED FALLAHAH |  |  |
| 164 | 2026-02-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 165 | 2026-02-23 | 1660.00 |  | I | 3051 | SALES | NOURA YASSIN ALFALAH |  |  |
| 166 | 2026-02-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 167 | 2026-02-23 | 500.00 |  | I | 3051 | SALES | MAGNUS NILSSON |  |  |
| 168 | 2026-02-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 169 | 2026-02-23 | 100.00 |  | I | 3051 | SALES | YOUSRA DALATI |  |  |
| 170 | 2026-02-23 | -1220.00 |  | O | 3051 | SALES_REFUND | Ikhlas Retur | Kund-namn på Lunar OUT = återbetalning av fö… |  |
| 171 | 2026-02-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 172 | 2026-02-24 | 379.00 |  | I | 3051 | SALES | AKHYAR YASSIN HASSAN MOHAMEDALI |  |  |
| 173 | 2026-02-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 174 | 2026-02-24 | 329.00 |  | I | 3051 | SALES | FATIMA ASAAD |  |  |
| 175 | 2026-02-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 176 | 2026-02-24 | 325.00 |  | I | 3051 | SALES | MILLION BERAKI |  |  |
| 177 | 2026-02-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 178 | 2026-02-24 | 200.00 |  | I | 3051 | SALES | AKHYAR YASSIN HASSAN MOHAMEDALI |  |  |
| 179 | 2026-02-24 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 180 | 2026-02-24 | 200.00 |  | I | 3051 | SALES | MONA FREJEH |  |  |
| 181 | 2026-02-25 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 182 | 2026-02-25 | 250.00 |  | I | 3051 | SALES | ABOUD,MARYAM |  |  |
| 183 | 2026-02-25 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 184 | 2026-02-25 | 599.00 |  | I | 3051 | SALES | ASAWER MUAYAD ORAIBI ORAIBI |  |  |
| 185 | 2026-02-25 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 186 | 2026-02-25 | 879.00 |  | I | 3051 | SALES | NADIA MORAD |  |  |
| 187 | 2026-02-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 188 | 2026-02-26 | 1782.00 |  | I | 3051 | SALES | MONA FREJEH |  |  |
| 189 | 2026-02-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 190 | 2026-02-26 | 179.00 |  | I | 3051 | SALES | AL KHALED,HANAA |  |  |
| 191 | 2026-03-02 | -3463.00 |  | O | 5700 | FREIGHT | Everygreen seaport fees |  |  |
| 192 | 2026-03-13 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 193 | 2026-03-13 | 978.00 |  | I | 3051 | SALES | Helen Zeresilasie Habte |  |  |
| 194 | 2026-03-13 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 195 | 2026-03-13 | 200.00 |  | I | 3051 | SALES | Helen Zeresilasie Habte |  |  |
| 196 | 2026-03-14 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 197 | 2026-03-14 | 7366.00 |  | I | 3051 | SALES | AL RASHID,SOMIA |  |  |
| 198 | 2026-03-15 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 199 | 2026-03-15 | 910.00 |  | I | 3051 | SALES | MONA FREJEH |  |  |
| 200 | 2026-03-15 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 201 | 2026-03-15 | 3000.00 |  | I | 3051 | SALES | MONA FREJEH |  |  |
| 202 | 2026-03-15 | -39.00 |  | O | 6570 | BANK_FEE | Swish Business enrollment |  |  |
| 203 | 2026-03-16 | -287.86 |  | O | 6540 | IT_SERVICES_NO_VAT | TWILIO.COM |  |  |
| 204 | 2026-03-17 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 205 | 2026-03-17 | 800.00 |  | I | 3051 | SALES | IBRAHEM HABASH |  |  |
| 206 | 2026-03-17 | -21911.00 |  | O | 1930 | INTERNAL_TRANSFER | Till 1930 | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 207 | 2026-03-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 208 | 2026-03-19 | 1159.00 |  | I | 3051 | SALES | MAHER ABDULSATER BOUZAN |  |  |
| 209 | 2026-03-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 210 | 2026-03-19 | 328.00 |  | I | 3051 | SALES | FARDOUSSA ADEN YOUSSOUF |  |  |
| 211 | 2026-03-19 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 212 | 2026-03-19 | 200.00 |  | I | 3051 | SALES | GENET KIBREAB WELDEMARYAM |  |  |
| 213 | 2026-03-19 | 1504.51 |  | I | 3051 | SALES | STRIPE Shopi |  |  |
| 214 | 2026-03-20 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 215 | 2026-03-20 | 1000.00 |  | I | 3051 | SALES | ABOUD,MARYAM |  |  |
| 216 | 2026-03-20 | 1040.80 |  | I | 3051 | SALES | STRIPE Shopi |  |  |
| 217 | 2026-03-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 218 | 2026-03-23 | 1079.00 |  | I | 3051 | SALES | Seham Saalouk |  |  |
| 219 | 2026-03-23 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 220 | 2026-03-23 | 360.00 |  | I | 3051 | SALES | AKHYAR YASSIN HASSAN MOHAMEDALI |  |  |
| 221 | 2026-03-25 | -7460.00 |  | O | 1930 | INTERNAL_TRANSFER | Transfer | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 222 | 2026-03-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 223 | 2026-03-26 | 200.00 |  | I | 3051 | SALES | ROIDA ALKLAH |  |  |
| 224 | 2026-03-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 225 | 2026-03-26 | 600.00 |  | I | 3051 | SALES | AWADYA SALEH |  |  |
| 226 | 2026-03-26 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 227 | 2026-03-26 | 898.00 |  | I | 3051 | SALES | AMIRA MOHAMAD |  |  |
| 228 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 229 | 2026-03-27 | 250.00 |  | I | 3051 | SALES | GHENA JARKAS |  |  |
| 230 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 231 | 2026-03-27 | 2750.00 |  | I | 3051 | SALES | GHENA JARKAS |  |  |
| 232 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 233 | 2026-03-27 | 1080.00 |  | I | 3051 | SALES | WEDAD MOHAMMAD |  |  |
| 234 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 235 | 2026-03-27 | 1050.00 |  | I | 3051 | SALES | HANIN ALAJLOUNI |  |  |
| 236 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 237 | 2026-03-27 | 200.00 |  | I | 3051 | SALES | HANIN ALAJLOUNI |  |  |
| 238 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 239 | 2026-03-27 | 200.00 |  | I | 3051 | SALES | NOUR MOKHLES AL MAHAMID |  |  |
| 240 | 2026-03-27 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 241 | 2026-03-27 | 200.00 |  | I | 3051 | SALES | WEDAD MOHAMMAD |  |  |
| 242 | 2026-03-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 243 | 2026-03-29 | 149.00 |  | I | 3051 | SALES | NTUMBA,SHUPETE |  |  |
| 244 | 2026-03-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 245 | 2026-03-29 | 650.00 |  | I | 3051 | SALES | FATEN AL SHLASH |  |  |
| 246 | 2026-03-29 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 247 | 2026-03-29 | 780.00 |  | I | 3051 | SALES | FATEN AL SHLASH |  |  |
| 248 | 2026-03-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 249 | 2026-03-30 | 79.00 |  | I | 3051 | SALES | OKBATEDROS,HIWET HANNES |  |  |
| 250 | 2026-03-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 251 | 2026-03-30 | 200.00 |  | I | 3051 | SALES | HANEEN ALQAHWAJI |  |  |
| 252 | 2026-03-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 253 | 2026-03-30 | 555.00 |  | I | 3051 | SALES | FIYORI YIKALO GILE |  |  |
| 254 | 2026-03-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 255 | 2026-03-30 | 200.00 |  | I | 3051 | SALES | AWADYA SALEH |  |  |
| 256 | 2026-03-30 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 257 | 2026-03-30 | 400.00 |  | I | 3051 | SALES | OKBATEDROS,HIWET HANNES |  |  |
| 258 | 2026-03-30 | -3000.00 |  | O | 1930 | INTERNAL_TRANSFER | To 1930 | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 259 | 2026-03-30 | -4400.00 |  | O | 1930 | INTERNAL_TRANSFER | Till 1930 | Intern överföring 1948 -> 1930 (matchas mot … |  |
| 260 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 261 | 2026-03-31 | 600.00 |  | I | 3051 | SALES | ALAMIN,AMNA MOHAMMEDALI |  |  |
| 262 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 263 | 2026-03-31 | 579.00 |  | I | 3051 | SALES | HIBA GHAZI |  |  |
| 264 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 265 | 2026-03-31 | 80.00 |  | I | 3051 | SALES | SOWIM MOHAMMAD |  |  |
| 266 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 267 | 2026-03-31 | 1600.00 |  | I | 3051 | SALES | SOWIM MOHAMMAD |  |  |
| 268 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 269 | 2026-03-31 | 1480.00 |  | I | 3051 | SALES | MARYNA RIELE WILLIAM WILLIAM |  |  |
| 270 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 271 | 2026-03-31 | 200.00 |  | I | 3051 | SALES | SARAB ALTAYAR |  |  |
| 272 | 2026-03-31 | -1.49 |  | O | 6570 | BANK_FEE | Fee |  |  |
| 273 | 2026-03-31 | 200.00 |  | I | 3051 | SALES | MARYNA RIELE WILLIAM WILLIAM |  |  |

---
_Genererad av `build_per_bank_audit.py` från `AUDIT_Q1_2026_FILL_REASONS.csv`._