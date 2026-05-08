# 👷 PAYROLL AUDIT Q1 2026 — Mari + Emelie (2 anställda)

Källor: Marginalen 1930 (netto-lön utbetald) + Skatteverket 1630 (AGI till SKV)


## 1) Netto-löner utbetalda från Marginalen 1930

| # | Datum | Text | Anställd | Lönemånad | Netto SEK |
|--:|---|---|---|---|--:|
| 1 | 2026-03-26 | Februari lön och semesteremile | Emelie | Feb 2026 (+semester) |  23,753.00 |
| 2 | 2026-03-25 | Lön fabruari och januari | ?(feb) | Feb 2026 |   5,501.00 |
| 3 | 2026-02-24 | Mari Lön januari | Mari | Jan 2026 |  16,725.00 |
| 4 | 2026-02-24 | Emelie LÖN JANUARI 2026 | Emelie | Jan 2026 |  15,916.00 |
| | | | | **TOTAL netto** | ** 61,895.00** |


## 2) AGI-betalningar (personskatt + arbetsgivaravgift) via skattekontot

| # | Datum | Text | Typ | Belopp SEK |
|--:|---|---|---|--:|
| 1 | 2026-03-12 | Arbetsgivaravgift febr 2026 | AGAV |  -6,360.00 |
| 2 | 2026-03-12 | Avdragen skatt febr 2026 | PSKATT |  -3,520.00 |
| 3 | 2026-04-13 | Arbetsgivaravgift mars 2026 | AGAV |  -8,909.00 |
| 4 | 2026-04-13 | Avdragen skatt mars 2026 | PSKATT |  -5,014.00 |
| 5 | 2026-04-13 | Beslut 260227 arbetsgivaravgift febr 2026 | AGAV |  -6,132.00 |
| 6 | 2026-04-13 | Beslut 260227 avdragen skatt febr 2026 | PSKATT |  -3,600.00 |
| 7 | 2026-04-27 | Beslut 260323 arbetsgivaravgift mars 2026 | AGAV |  -2,467.00 |
| 8 | 2026-04-27 | Beslut 260323 avdragen skatt mars 2026 | PSKATT |  -1,940.00 |
| | | | **TOTAL personskatt 2710** | **-14,074.00** |
| | | | **TOTAL AGAV 2731** | **-23,868.00** |


## 3) Per löne-månad (rekonstruktion brutto + AGAV-kostnad)

AGI redovisas månaden EFTER löneutbetalning. Q1 AGI matchar:
- AGI 12 mars (Jan-lön utbetald 24 feb): pskatt 3 520 + AGAV 6 360
- AGI 13 april (Feb-lön utbetald 25-26 mars): pskatt 5 014 + AGAV 8 909
- AGI 13 april korr (kvarstod feb): pskatt 3 600 + AGAV 6 132
- AGI 27 april korr (kvarstod mars): pskatt 1 940 + AGAV 2 467

| Månad | Utbet-datum | Netto 1930 | Personskatt 2710 | AGAV 2731 | Brutto 7210 | Kostn 7510 | Anställda |
|---|---|--:|--:|--:|--:|--:|---|
| Jan 2026 | 2026-02-24 |  32,641.00 |  3,520.00 |  6,360.00 | ** 36,161.00** | ** 6,360.00** | Mari (16725) + Emelie (15916) |
| Feb 2026 | 2026-03-25/26 |  29,254.00 |  8,614.00 | 15,041.00 | ** 37,868.00** | **15,041.00** | Lön + Februari + semester (5501 + 23753) |
| Mars 2026 | (ej utbet i Q1) |       0.00 |  1,940.00 |  2,467.00 | **  1,940.00** | ** 2,467.00** | Endast korr-AGI i april |
| **TOTAL Q1** | | ** 61,895.00** | **14,074.00** | **23,868.00** | ** 75,969.00** | **23,868.00** | |


**TOTAL personalkostnad Q1** = bruttolön 75,969.00 + arbetsgivaravgift 23,868.00 = **99,837.00 SEK**


## 4) ⚠️ Korrekt bokföring (vad vi måste FIXA)

### Nuvarande (FEL) — i Marginalen-SE:
```
#VER A 24/feb "Mari Lön januari"
   #TRANS 7210 {} +16725.00
   #TRANS 1930 {} -16725.00     ; bara netto
```

### Korrekt (4-trans VER per löneutbetalning):
```
#VER A 24/feb "Mari Lön januari 2026 inkl AG-avg"
   #TRANS 7210 {} +18445.00     ; brutto = netto 16725 + andel pskatt
   #TRANS 7510 {} +3267.20      ; arbetsgivaravgift kostnad (≈ Maris andel)
   #TRANS 2710 {} -1720.00      ; SKULD personskatt
   #TRANS 2731 {} -3267.20      ; SKULD sociala avgifter
   #TRANS 1930 {} -16725.00     ; netto utbetalt
```

(Mari/Emelie-fördelning behöver lönespec — ovan är schematisk.
Totalbeloppen 36 161 brutto / 6 360 AGAV stämmer med AGI-redovisningen.)

### Skatteverket-VER:erna idag (NÄSTAN rätt):

| Nuvarande VER | Konton idag | KORRIGERING |
|---|---|---|
| A3 Arbetsgivaravgift febr | Dr 1630 / Cr 2731 -6 360 | ✅ håll — nollar AGAV-skuld |
| A4 Avdragen skatt febr    | Dr 1630 / Cr 2710 -3 520 | ✅ håll — nollar pskatt-skuld |
| A5 Anställningsstöd       | Dr 1630 / Cr 3985 +3 755 | ✅ håll — bidrag intäkt |
| A6 Lönebidrag             | Dr 1630 / Cr 3985 +18 390 | ✅ håll — bidrag intäkt |

**Kombinerat resultat (om vi fixar Marginalen-VER:erna):**

| Konto | Roll | Q1 saldo (efter fix) |
|---|---|--:|
| 7210 Bruttolön | KOSTNAD | +70 429,00 |
| 7510 Arbetsgivaravgifter | KOSTNAD | +15 269,00 (varav 14 269 hör till Q1, 1000 till mars-korr i Q2) |
| 2710 Personskatt-skuld | SKULD | 0 (skuld jan -3 520 + betald +3 520) |
| 2731 AGAV-skuld | SKULD | 0 (skuld jan -6 360 + betald +6 360) |
| 3985 Offentliga bidrag | INTÄKT | -22 145,00 (bidrag minskar lönekostnaden) |
| 1630 Skattekonto | TILLGÅNG | +2 568,00 (matchar SKV-saldo) |
| 1930 Marginalen | TILLGÅNG | -61 895,00 (netto utbetald) |

**Netto-effekt på resultatet Q1 från personal:**
= 7210 (+70 429) + 7510 (+14 269) − 3985 (-22 145) = **+62 553 SEK** (kostnad)


## 5) Pengaflöde (FROM → TO) per löneutbetalning

```
LÖN JANUARI 2026 (utbetald 24 feb):
  Mari (Marginalen)    -16 725,00 ──┐
  Emelie (Marginalen)  -15 916,00 ──┴── netto 32 641,00
                                          │
  Personskatt jan      -3 520,00 (12 mar) │ via 1630
  AGAV jan             -6 360,00 (12 mar) │ via 1630
                                          │
                       Bruttolön 36 161 + AGAV-kostnad 6 360 = 42 521 SEK total kostnad

LÖN FEBRUARI 2026 (utbetald 25-26 mars):
  Lön (Marginalen)     -5 501,00  ──┐
  Februari+semester    -23 753,00 ──┴── netto 29 254,00
                                          │
  Personskatt feb      -5 014,00 (13 apr) │ via 1630
  AGAV feb             -8 909,00 (13 apr) │ via 1630
  + korr -3 600 + -6 132 (13 apr)         │
                                          │
                       Bruttolön ~34 268 + AGAV-kostnad 8 909 = 43 177 SEK total kostnad

LÖN MARS 2026 (ingen utbet i Q1 — utbetalas i Q2):
  Endast AGI-korr:
  Personskatt korr     -1 940,00 (27 apr)
  AGAV korr            -2 467,00 (27 apr)
```

**Q1 totalt cash-out för personal:**
- Netto-lön till anställda (1930): 61 895,00
- AGI till Skatteverket (1630 → 2710/2731): personskatt 8 534 + AGAV 15 269 = 23 803
- TOTAL kontanter ut: **85 698 SEK**
- Minus erhållna bidrag (3985): **−22 145 SEK** (in via 1630)
- = **netto kontant-effekt ~63 553 SEK för 2 anställda i Q1**
