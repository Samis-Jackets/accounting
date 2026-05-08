# Skatteverket 1630 — FULL audit Q1 2026 (CSV vs SE)

Källa CSV: `Bokförda transaktioner 559489-5301 Alla typer 2026-01-01--2026-05-02.csv`  |  Källa SE: `SKATTEVERKET_STANDALONE.se`

IB 2026-01-01: **108.00 SEK**  |  UB CSV 2026-05-02: **12,407.00 SEK**


## 1) Hela CSV one-by-one

| # | Datum | Belopp | Saldo | → Konto | Motkonto | Kategori | I SE? | Kommentar |
|--:|---|--:|--:|---|---|---|:-:|---|
| 1 | 2026-02-12 | -81,643.00 | -81,535.00 | 1630 | 2650 | MOMS | ✅ | Momsinbetalning kvartal |
| 2 | 2026-02-28 |  19,612.00 | -61,923.00 | 1630 | 1930 | INB | 🔁 (Marginalen) | Inbetalning från 1930 Marginalen — BOKAS I MARGINALEN-SE (skip här) |
| 3 | 2026-03-01 |    -645.00 | -62,568.00 | 1630 | 8423 | RÄNTA | ✅ | Kostnadsränta skattekonto |
| 4 | 2026-03-12 |  -6,360.00 | -68,928.00 | 1630 | 2731 | AGAV | ✅ | Arbetsgivaravgift (sociala avgifter) — bör motsvara accruerad 2731 från löne-VER |
| 5 | 2026-03-12 |  -3,520.00 | -72,448.00 | 1630 | 2710 | PSKATT | ✅ | Personalskatt (innehållen) — bör motsvara accruerad 2710 från löne-VER |
| 6 | 2026-03-12 |   3,755.00 | -68,693.00 | 1630 | 3985 | BIDRAG | ✅ | Anställningsstöd (offentligt bidrag) |
| 7 | 2026-03-12 |  18,390.00 | -50,303.00 | 1630 | 3985 | BIDRAG | ✅ | Lönebidrag/skyddat arbete (offentligt bidrag) |
| 8 | 2026-03-19 |  52,871.00 |   2,568.00 | 1630 | 1930 | INB | 🔁 (Marginalen) | Inbetalning från 1930 Marginalen — BOKAS I MARGINALEN-SE (skip här) |
| 9 | 2026-04-04 |    -475.00 |   2,093.00 | 1630 | 8423 | RÄNTA | ⏭️ Q2 | Kostnadsränta skattekonto |
| 10 | 2026-04-04 |       2.00 |   2,095.00 | 1630 | 8314 | RÄNTA | ⏭️ Q2 | Intäktsränta skattekonto |
| 11 | 2026-04-13 |  -8,909.00 |  -6,814.00 | 1630 | 2731 | AGAV | ⏭️ Q2 | Arbetsgivaravgift (sociala avgifter) — bör motsvara accruerad 2731 från löne-VER |
| 12 | 2026-04-13 |  -5,014.00 | -11,828.00 | 1630 | 2710 | PSKATT | ⏭️ Q2 | Personalskatt (innehållen) — bör motsvara accruerad 2710 från löne-VER |
| 13 | 2026-04-13 |  -6,132.00 | -17,960.00 | 1630 | 2731 | AGAV | ⏭️ Q2 | Arbetsgivaravgift (sociala avgifter) — bör motsvara accruerad 2731 från löne-VER |
| 14 | 2026-04-13 |  -3,600.00 | -21,560.00 | 1630 | 2710 | PSKATT | ⏭️ Q2 | Personalskatt (innehållen) — bör motsvara accruerad 2710 från löne-VER |
| 15 | 2026-04-13 |  18,314.00 |  -3,246.00 | 1630 | 3985 | BIDRAG | ⏭️ Q2 | Anställningsstöd (offentligt bidrag) |
| 16 | 2026-04-13 |  20,060.00 |  16,814.00 | 1630 | 3985 | BIDRAG | ⏭️ Q2 | Lönebidrag/skyddat arbete (offentligt bidrag) |
| 17 | 2026-04-27 |  -2,467.00 |  14,347.00 | 1630 | 2731 | AGAV | ⏭️ Q2 | Arbetsgivaravgift (sociala avgifter) — bör motsvara accruerad 2731 från löne-VER |
| 18 | 2026-04-27 |  -1,940.00 |  12,407.00 | 1630 | 2710 | PSKATT | ⏭️ Q2 | Personalskatt (innehållen) — bör motsvara accruerad 2710 från löne-VER |

Beräknat saldo CSV vid 2026-03-31: **2,568.00 SEK**
Beräknat saldo CSV vid 2026-05-02: **12,407.00 SEK** (CSV uppger 12,407.00)


## 2) Vad finns i SKATTEVERKET_STANDALONE.se

| Ver | Datum | Text | Trans (konto / belopp) |
|---|---|---|---|
| A1 | 20260212 | Moms okt 2025 - dec 2025 | 1630 -81,643.00 ; 2650 +81,643.00 |
| A2 | 20260301 | Kostnadsränta | 1630    -645.00 ; 8423    +645.00 |
| A3 | 20260312 | Arbetsgivaravgift febr 2026 | 1630  -6,360.00 ; 2731  +6,360.00 |
| A4 | 20260312 | Avdragen skatt febr 2026 | 1630  -3,520.00 ; 2710  +3,520.00 |
| A5 | 20260312 | Anställningsstöd | 1630  +3,755.00 ; 3985  -3,755.00 |
| A6 | 20260312 | Lönebidrag och skyddat arbete | 1630 +18,390.00 ; 3985 -18,390.00 |

1630-rörelse i SE: **-70,023.00 SEK**
Plus inbetalningar från Marginalen (rad 88 + 104) — 1630-sida: **+72 483,00 SEK** (1930-sida: -72 483,00)
Beräknat 1630 UB Q1 från IB 108: **2,568.00 SEK**
CSV 1630 saldo 2026-03-19 (sista Q1-rad): **2 568,00 SEK** → ✅ MATCH om beräknat = 2568,00


## 3) ⚠️ Lön / personskatt / arbetsgivaravgift — METODFEL


**Nuvarande metod (FEL):**
- Marginalen 1930 betalar bara NETTO-lön → debet 7210 / kredit 1930.
- Skatteverket-SE bokar Avdragen skatt → debet 2710 / kredit 1630, och
  Arbetsgivaravgift → debet 2731 / kredit 1630.
- 2710 och 2731 får DEBET-saldo (=tillgång) trots att de är skuldkonton →
  felaktigt; det ska ha funnits en KREDIT (skuld) först som nu rensas.

**Konsekvens:**
- 7210 underdrives med personskatt-beloppet (gross under-reported).
- 7510 (arbetsgivaravgift kostnad) bokas INTE alls → resultaträkningen saknar
  social-kostnad, kostnaden hamnar fel i 2731 som ett "negativt skuld".
- 2710 och 2731 visar fel saldon i balansräkningen.

**Korrekt metod (svensk standard):**

För varje löneutbetalning i 1930 ska VER innehålla:
```
#VER A x YYYYMMDD "Lön Mari Jan 2026 + arbetsgivaravgifter"
{
   #TRANS 7210 {} +Bruttolön                 ; lönekostnad (brutto)
   #TRANS 7510 {} +Arbetsgivaravgift          ; social-kostnad (~10,21% första anst.)
   #TRANS 2710 {} -Personskatt                ; SKULD personalskatt
   #TRANS 2731 {} -Arbetsgivaravgift          ; SKULD sociala avgifter
   #TRANS 1930 {} -Nettolön                   ; betalt från bank
}
```

Sedan när skattekontot betalar (det vi har idag är OK):
```
#VER A y YYYYMMDD "Avdragen skatt febr 2026"
{
   #TRANS 1630 {} -Personskatt
   #TRANS 2710 {} +Personskatt    ; nollar skulden
}
#VER A z YYYYMMDD "Arbetsgivaravgift febr 2026"
{
   #TRANS 1630 {} -Arbetsgivaravgift
   #TRANS 2731 {} +Arbetsgivaravgift  ; nollar skulden
}
```

**Avstämning Q1 2026 (per AGI-redovisning till SKV):**

| Månad | Personskatt 2710 | AGAV 2731 | Implied bruttolön (netto+pskatt) |
|---|--:|--:|--:|
| Jan-lön (utbetald 24 feb)      | 3 520 | 6 360 | 32 641 + 3 520 = **36 161** |
| Feb-lön (utbetald 25-26 mars)  | 5 014 | 8 909 | 29 254 + 5 014 = **34 268** |

AGAV-procent jan: 6360 / 36161 = 17,6 % (reducerad – första anställd?)
AGAV-procent feb: 8909 / 34268 = 26,0 % (närmare ordinarie 31,42 %)

⚠️ **Att åtgärda för bokslutet:**
1. Lägg till accrual-VER för jan-lön och feb-lön på Marginalen utbetalningsdatum
   som bokar bruttolön (7210), arbetsgivaravgift kostnad (7510 eller 7514 första anst.),
   personskatt-skuld (2710), AGAV-skuld (2731), och nettolön (1930).
2. Behåll nuvarande Skatteverket-VER:erna för betalning till skattekonto (de
   nollar skulderna när AGI-betalningen sker).
3. Resultat: 7210/7510 visar full kostnad, 2710/2731 stänger ned till noll,
   1630 stämmer mot Skatteverkets saldolista.



## 4) ✅ Anställningsstöd & Lönebidrag → 3985 (korrekt)


Båda är offentliga bidrag (Arbetsförmedlingen). BAS-konto **3985 Erhållna
offentliga bidrag** är rätt. De krediteras (ökar intäkt) när skattekontot
ökar (debet 1630).

| Datum | Typ | Belopp | Hanterat? |
|---|---|--:|:-:|
| 2026-03-12 | Anställningsstöd | +3 755,00 | ✅ VER A5 |
| 2026-03-12 | Lönebidrag/skyddat arbete | +18 390,00 | ✅ VER A6 |
| 2026-04-13 | Anställningsstöd | +18 314,00 | ⏭️ Q2 |
| 2026-04-13 | Lönebidrag/skyddat arbete | +20 060,00 | ⏭️ Q2 |

**Kontroll mot Arbetsförmedlingen-mappar:** se `Arbetsförmedlinigen/` och
`financials/arbetsformedlingen/` för beslut/utbetalningsavier för matchning.


## 5) ✅ Moms okt-dec 2025 (-81 643) → debet 2650 / kredit 1630


Detta är betalning av moms-skuld från Q4 2025. För att VER A1 ska balansera
korrekt i master-filen krävs att **2650 har en KREDIT-IB på 81 643 SEK** från
prior period (annars hamnar 2650 på debet-saldo).

Nuvarande SKATTEVERKET_STANDALONE.se: `#IB 0 2650 0.00` — detta är OK för
standalone-import men måste **ersättas av riktig IB från 2025-Q4-bokslut**
när vi mergar till master Q1.

**Verifierat IB-behov:** 2650 IB 2026-01-01 ska vara **−81 643,00 SEK**
(skuld till SKV) baserat på Q4 2025 momsdeklaration.


## 6) ✅ Räntor → 8423 / 8314


| Datum | Typ | Belopp | Konto | Hanterat? |
|---|---|--:|---|:-:|
| 2026-03-01 | Kostnadsränta | -645 | 8423 | ✅ VER A2 |
| 2026-04-04 | Kostnadsränta | -475 | 8423 | ⏭️ Q2 |
| 2026-04-04 | Intäktsränta  | +2   | 8314 (eller 8313) | ⏭️ Q2 |

Notera: 8314 = Ränteintäkter från omsättningstillgångar. Kontot fanns inte i
KONTO-deklarationen — lägg till vid Q2-bygget.



## 7) ✅ LÖN — Mari & Emelie Q1 2026 — FULL AUDIT (uppdaterad 2026-05-04)

**STATUS: KORREKT.** Alla löner i `MARGINALEN_STANDALONE.se` följer svensk standard
(BAS-konto-praxis enligt Bokföringsnämnden / Skatteverket). 100 % match mot AGI.

### 7.1 Bokföringsmetod (svensk standard för lön)

För varje löneutbetalning från företagskontot (1930) bokförs **5 transaktioner**:

```
#VER A x YYYYMMDD "<beskrivning>"
{
   #TRANS 7210 {} +Bruttolön            ; lönekostnad (debet, R)
   #TRANS 7510 {} +Arbetsgivaravgift     ; soc-kostnad ~10,21 % första anst.
                                         ; eller 31,42 % ordinarie (debet, R)
   #TRANS 2710 {} -Personskatt           ; SKULD personalskatt (kredit, B)
   #TRANS 2731 {} -Arbetsgivaravgift     ; SKULD sociala avgifter (kredit, B)
   #TRANS 1930 {} -Nettolön              ; betalt från Marginalen (kredit, B)
}
```

**Balanseringsregel:** `7210 + 7510 + 2710 + 2731 + 1930 = 0`
(Brutto + AGAV-kostnad = Netto + Pskatt-skuld + AGAV-skuld)

Sedan när Skatteverket drar AGI-betalningen från skattekontot (bokas i
`SKATTEVERKET_STANDALONE.se`):

```
#VER A y YYYYMMDD "Avdragen skatt MMMM ÅÅÅÅ"
{ #TRANS 1630 {} -Personskatt    #TRANS 2710 {} +Personskatt }    ; nollar 2710

#VER A z YYYYMMDD "Arbetsgivaravgift MMMM ÅÅÅÅ"
{ #TRANS 1630 {} -AGAV           #TRANS 2731 {} +AGAV         }    ; nollar 2731
```

### 7.2 Q1 2026 lön-rörelser i MARGINALEN_STANDALONE.se

| VER | Datum | Mottagare / Beskrivning | 7210 brutto | 7510 AGAV | 2710 pskatt | 2731 AGAV | 1930 netto |
|---|---|---|--:|--:|--:|--:|--:|
| A79 | 2026-02-24 | Mari Lön januari               | 18 528,76 |  3 258,27 | -1 803,76 |  -3 258,27 | -16 725,00 |
| A80 | 2026-02-24 | Emelie LÖN JANUARI 2026        | 17 632,24 |  3 101,73 | -1 716,24 |  -3 101,73 | -15 916,00 |
| A105| 2026-03-25 | Lön februari och januari       |  7 121,08 |  2 828,78 | -1 620,08 |  -2 828,78 |  -5 501,00 |
| A107| 2026-03-26 | Februari lön och semester Emil | 30 746,92 | 12 212,22 | -6 993,92 | -12 212,22 | -23 753,00 |
| **TOTAL** | | | **74 029,00** | **21 401,00** | **-12 134,00** | **-21 401,00** | **-61 895,00** |

### 7.3 AGI-MATCH mot Skatteverket (kors-verifiering)

| Period | Netto utbet (Marg) | Pskatt accrual | AGAV accrual | SKV-AGI faktisk pskatt | SKV-AGI faktisk AGAV | AGI-redovisn | Match |
|---|--:|--:|--:|--:|--:|---|:-:|
| Feb-utbet (Q1)   | 32 641,00 | 3 520,00 |  6 360,00 |  3 520,00 |  6 360,00 | 12 mars 2026  | ✅✅ |
| Mars-utbet (Q1)  | 29 254,00 | 8 614,00 | 15 041,00 |  8 614,00 | 15 041,00 | 13 april 2026 (Q2 ⏭️) | ✅✅ |

**Verifierat:** 100,00 % match — pskatt och AGAV som accrueras i Marginalen
matchar exakt det Skatteverket faktiskt drar i AGI-redovisningen.

### 7.4 Skattekonto-kvittningar (1630 i SKATTEVERKET_STANDALONE.se)

| Ver | Datum | Belopp 1630 | Motkonto | Effekt |
|---|---|--:|---|---|
| A3 | 2026-03-12 | -6 360,00  | 2731 | Nollar feb-AGAV-skuld ✅ |
| A4 | 2026-03-12 | -3 520,00  | 2710 | Nollar feb-pskatt-skuld ✅ |
| —  | 2026-04-13 | -15 041,00 | 2731 | Nollar mars-AGAV-skuld (Q2 ⏭️) |
| —  | 2026-04-13 | -8 614,00  | 2710 | Nollar mars-pskatt-skuld (Q2 ⏭️) |

**Saldon per 2026-03-31:**
- 2710: -12 134 (Marg) + 3 520 (SKV-A4) = **-8 614** (skuld kvar för mars-utbet → kvittas 13 april)
- 2731: -21 401 (Marg) + 6 360 (SKV-A3) = **-15 041** (skuld kvar för mars-utbet → kvittas 13 april)

Båda restskulderna **kvittas exakt** av AGI-betalningarna i Q2.

### 7.5 Inbetalningar 1930 → 1630 (skattekonto-fyllning från Marginalen)

| Ver | Datum | Belopp | Bokning | Texthistorik bank |
|---|---|--:|---|---|
| (Marg) | 2026-02-27 | 19 612,00 | 1630 D / 1930 K | "Emelie och Mari skrattar" (memo) |
| (Marg) | 2026-03-18 | 52 871,00 | 1630 D / 1930 K | "moms ocha rbetsgivare" (memo) |

**OBS:** Bankraden 27 feb innehåller texten "Emelie och Mari skrattar" men beloppet
19 612 matchar **exakt** SKV-CSV-raden 28 feb (en banks valuteringsdag = nästa
bankdag). Detta är **inbetalning till skattekontot**, inte en lön. Korrekt
bokad redan (1630 D / 1930 K).

### 7.6 Bevis och kontrollscript

Kör: `..\.venv\Scripts\python.exe audit_payroll_vs_skv.py`

Förväntat: alla 4 MATCH-rader ✅ (Feb pskatt/AGAV, Mar pskatt/AGAV).

### 7.7 SE-fil — Skatteverket-kompatibilitet (SIE4)

`SKATTEVERKET_STANDALONE.se` följer **SIE4-standarden** (Bokföringsnämnden,
BAS 97 / EUBAS97):

- `#FORMAT PC8` (cp437-encoding)
- `#KPTYP EUBAS97`
- CRLF-radslut
- `#RAR 0` aktuellt räkenskapsår + `#RAR -1` föregående
- `#KONTO`-deklaration för alla använda konton (1630, 2650, 2710, 2731, 3985, 8423)
- `#IB 0 1630 108.00` (öppningsbalans skattekonto från SKV-saldolista)

Filen kan läsas direkt in i Visma eAccounting via **Inställningar →
Importera SIE-fil**, samt i alla andra svenska bokföringssystem som stöder SIE4
(Fortnox, BL, eEkonomi, Speedledger m.fl.).

### 7.8 Slutsats

| Kontroll | Status |
|---|:-:|
| 5-trans-accrual per löneutbetalning | ✅ |
| Brutto + AGAV-kostnad bokfört (R) | ✅ |
| Pskatt-skuld 2710 öppnad i Marg, stängd av SKV | ✅ för feb, ⏭️ Q2 för mars |
| AGAV-skuld 2731 öppnad i Marg, stängd av SKV | ✅ för feb, ⏭️ Q2 för mars |
| AGI-belopp matchar SKV exakt (öre) | ✅ 100 % |
| SE-fil SIE4-kompatibel för Visma-import | ✅ |
| Inbetalningar 1930→1630 (skattekonto-fyllning) | ✅ 2 st (19 612 + 52 871) |

**Inga ändringar krävs i Q1 2026.** Alla Mari/Emelie-löner och alla
Skatteverket-kvittningar är fullständigt och korrekt bokförda enligt
svensk redovisningsstandard.
