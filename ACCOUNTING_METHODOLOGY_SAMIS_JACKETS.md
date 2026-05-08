# Samis Jackets AB — Bokföringsmetodik & affärsregler

**Org.nr:** 559489-5301  
**Räkenskapsår:** Brutet (juli–juni) — period i denna fil: 2026-01-01 → 2026-03-31  
**Kontoplan:** EU-BAS97 (svensk standard)  
**Skapad:** 2026-04-28 — **Gäller alla perioder** om inget annat sägs.

> Detta dokument beskriver hur vi (Sami) tänker kring företagets transaktioner.
> Skripten i denna mapp följer reglerna nedan. Om en regel ändras → uppdatera
> både detta dokument och `build_audit_csv.py` (sökning: `PATTERNS`).

---

## 1. Bankkonton

| BAS-konto | Bank | Typ | Beskrivning |
|---|---|---|---|
| **1930** | Marginalen Bank | Företag | Huvudkonto. Worldline-payouts, leverantörsbetalningar, Swish |
| **1947** | Worldline | Företag | POS-kortterminal. Settlement går vidare till 1930 |
| **1948** | Lunar Bank | Företag | **Säljkonto only** – Shopify/Swish-inkomster |
| **1944** | Wise EUR | Företag | Internationella betalningar |
| **1945** | Wise SEK | Företag | Internationella betalningar |
| **1942** | Wise USD | Företag | Internationella betalningar |
| **1943** | Wise GBP | Företag | Internationella betalningar |
| **1940** | Wise TRY | Företag | Turkiska leverantörer |
| **1949** | Wise CNY | Företag | Kinesiska leverantörer |
| **2893** | Skuld till närstående (Sami / familj) | Privat | Nordea Gold/Premium/Personkonto + Amex + Remember Card är privata |

---

## 2. Klassificeringsregler (gäller alla perioder)

### 2.1 Lunar Bank (1948) — säljkonto

| Riktning | Regel | Konto |
|---|---|---|
| **IN** | Allt är försäljning (Shopify / Swish / kortterminal) | **3051** moms 25% |
| **OUT** med text `Till 1930`, `To 1930`, `Transfer`, `Insättning`, `Överföring`, `Swish sales`, `Sweish sales` | Intern överföring till Marginalen | **D 1930 / K 1948** |
| **OUT** med kundnamn (t.ex. `Najma Dayib`, `Ikhlas Retur`, `Retur refund`) | **Återbetalning av försäljning** (kunden returnerade vara) | **D 3051 (-) / K 1948** moms 25% |
| **OUT** med text `Lunar Plan Essential` | Bankavgift månadsabonnemang | **6570** |
| **OUT** med text `Swish Business enrollment` | Bankavgift Swish | **6570** |
| **OUT** med leverantörsnamn (Twilio, One.com, Everygreen seaport, etc.) | Driftskostnad enligt leverantörstyp | varierar |
| **OUT** `2893 återbetalning` | Återbetalning av lån till närstående | **2893** |

### 2.2 Marginalen (1930) — företagets huvudkonto

| Mönster | Konto | Kommentar |
|---|---|---|
| `B` + 8–12 siffror (B01310359414 etc.) | **1947** | Worldline-payout — matchar daglig settlement på Payouts-fliken |
| `Swish sales`, `Sweish sales`, `Swish inbetalning` | **3051** moms 25% | Direktförsäljning Swish |
| `From 2893`, `To 2893`, `2893`, `Sami`, `Mohammad Sami` | **2893** | Skuld till närstående (Sami / familj) |
| `Mohamad Sharif A Qalaji` | **3105** moms **0%** | **Export Norge** — vi har inte tagit ut moms |
| Leverantörsnamn → tabell 2.4 | enligt typ | |

### 2.3 Wise (1940/1942/1943/1944/1945/1949) — internationella konton

> **VIKTIGT:** Alla Wise-rader vars `description` eller `counterparty` innehåller
> ordet `wise` (eller är `Topped up account`, `Money added`, `Transfer to/from
> wise`) är **interna företagsöverföringar** mellan våra egna bankkonton.

| Wise-mönster | Konto | Kommentar |
|---|---|---|
| `wise`, `topped up account`, `money added`, `sent money to <own name>` | **1940/1942/1943/1944/1945/1949** (motkonto = annat eget bankkonto) | Intern överföring – ingen kostnad |
| `Converted X to Y` | **3960** valutakursvinst / **7960** valutakursförlust | FX-konvertering inom Wise |
| Övrigt OUT (Parking, hotell, restaurang, leverantör) | enligt 2.4 | Affärskostnader utomlands |

### 2.4 Leverantörs-/kostnadsregister

| Motpart / mönster | Konto | Moms | Kategori |
|---|---|---:|---|
| **Fastighets AB Akvarium** | **5010** | 25% | **Hyra för lager/butik** |
| **SVEA BANK AB** | **6570** | 0% | **Månadskostnad kortterminal** |
| **Worldline / Bambora** fees | **6570** | 0% | Korttransaktionsavgifter |
| **Lunar Plan Essential** | **6570** | 0% | Bankabonnemang |
| **Twilio.com** | **6540** | 0% | IT-tjänster utland |
| **One.com** | **6540** | 25% | Hosting |
| **Vimla** (mobilabonnemang) | **6212** | 25% | **Företagets mobilabonnemang** |
| **Apple.com / App Store** | **5420** | 0% | Programvara utland |
| **Google / GSuite / YouTube** | **5420** | 0% | Programvara utland |
| **Meta / Facebook / TikTok / Snapchat** | **5900** | 0% | Marknadsföring digital |
| **Shopify** | **6500** | 25% | E-handelsplattform |
| **Schenker / DSV / DHL / UPS / FedEx / PostNord / Unitrans / Container / Everygreen seaport** | **5700** | 25% | Frakt / sjöfrakt |
| **Future World Tech (FWT)** | **2441** | 0% | Leverantörsskuld – varuinköp |
| **Klarna autogiro K\*** | **2893** | 0% | Privat (Sami) |
| **Willys/Coop/ICA/Lidl** | privat | — | Mat |

### 2.5 Lön och personal

| Person | Roll | Konto |
|---|---|---|
| **Emilie** | Anställd | **7210** lön + **7510** arbetsgivaravgifter (31,42%) + **2710** prelskatt |
| **Mari** | Anställd | **7210** lön + **7510** arbetsgivaravgifter + **2710** prelskatt |

Bokföringsexempel (bruttolön 25 000 kr):
```
D 7210  25 000        (bruttolön)
K 1930  17 950        (nettolön till anställd)
K 2710   7 050        (prelskatt 28,2 %)
D 7510   7 855        (arbetsgivaravgifter 31,42 %)
K 2730   7 855        (skuld arbetsgivaravgifter)
```

### 2.6 Privatkonton (Nordea Gold / Premium / Personkonto + Amex + Remember Card)

> Alla Nordeas 3 konton är **privata** men används ofta för företagets utgifter
> eftersom Sami betalar och bolaget är skyldigt honom (2893).

| Riktning | Regel |
|---|---|
| Privat utgift | Påverkar inte bolagets bokföring |
| Företagsutgift på privat kort | **D <kostnadskonto> / K 2893** (bolaget är skyldigt Sami) |
| Insättning till företaget från Sami | **D 1930 / K 2893** |
| Återbetalning från företaget till Sami | **D 2893 / K 1930** |

Allt som heter eller refererar till **2893** / **near people loans** /
`Mohammad Sami`, `Mohammed Ali`, `Alaa`, `Sharif` (förutom Mohamad Sharif A Qalaji
som är Norge-export-kund) bokas som skuld till närstående **2893**.

---

## 3. Verifikationsserier (förslag för Visma)

| Serie | Användning |
|---|---|
| A | Marginalen 1930 (huvudbank) |
| B | Lunar 1948 |
| W | Wise (alla valutor) |
| N | Worldline POS |
| L | Lön / personal |
| M | Manuella justeringar / periodiseringar |

---

## 3.5 Valutahantering (Wise EUR/USD/GBP/TRY/CNY)

**Regel (från `accounting_rules/KONTOPLAN_OCH_BOKFORINGSREGLER.md`):**
> "ALLTID bokför i SEK-värdet, inte utländskt belopp!"

`build_audit_csv.py` räknar därför om ALLA Wise-rader till SEK med Q1 2026
genomsnittskurser (i `FX_RATES_TO_SEK`):

| Valuta | Kurs (→SEK) | BAS-konto |
|---|---:|---|
| USD | **9,40** | 1942 |
| EUR | 11,30 | 1944 |
| GBP | 13,40 | 1943 |
| TRY | 0,30 | 1940 |
| CNY | 1,30 | 1949 |
| SEK | 1,00 | 1945 |

Varje rad får en **note**: `Wise USD 11416.82 × 9.40 = 107318.11 SEK
(genomsnittskurs Q1 2026)` så revisor ser original + kurs.

Eventuell skillnad mellan kurs vid bokförings­datum och faktisk Wise-omräkning
bokas på **8331** (kursvinst) eller **7960** (kursförlust).

---

## 3.6 Future World Tech International Limited (Kina) — varuinköp

**Regel:** Alla betalningar till `FUTURE WORLD TECH INTERNATIONAL LIMITED`
(via Wise USD) är **lager-anskaffning från Kina**.

- **Konto 1460** (Lager varor) — debet
- **Konto 2440** (Leverantörsskuld) — kredit på fakturadag, sen
  debiteras 2440 / krediteras 1942 vid varje Wise-betalning.
- **Moms:** 0% (utanför EU, ingen ingående moms i Sverige — moms tas vid tull
  via tullräkning från Tullverket, bokas separat på 2645).

**Q1 2026 specifikt:** containerinköp på **126 882,90 USD = 1 192 699,26 SEK**
(kurs 9,40). Betalningarna skedde över flera kvartal — se
`FUTURE_WORLD_TECH_INVENTORY.md`.

---

## 4. Periodvis arbetsflöde

```
1. source_csv/ får råfiler (banker + Worldline xlsx + sales)
2. build_audit_csv.py        → AUDIT_..._FILL_REASONS.csv
3. build_audit_md.py         → AUDIT_..._FILL_REASONS.md  (människoläsbar)
4. verify_audit.py           → AUDIT_VERIFICATION_REPORT.md (datum/antal/summa)
5. match_transfers.py        → TRANSFER_MATCHING_LUNAR_MARGINALEN.md
6. match_nordea_marginalen.py → NORDEA_MARGINALEN_MATCHING.md
7. build_review_md.py        → NEEDS_REVIEW_*.md + NORDEA_FULL_AUDIT_*.md
8. nordea_full_extract.py    → NORDEA_RAW_*.md + NORDEA_FINAL_CATEGORIZED.md
9. build_wise_lunar_final.py → WISE_FINAL_AUDIT_*.md + LUNAR_FINAL_AUDIT_*.md
                                + FUTURE_WORLD_TECH_INVENTORY.md
10. Sami fyller i NEEDS_REVIEW   (B / P / [konto:XXXX])
11. build_se.py              → final_se_files/PERIOD_COMPLETE.se  (Visma SIE4)
```
