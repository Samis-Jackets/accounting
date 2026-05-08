# Wise USD – Metodik (CSV → SE → Visma)

**Bolag:** Samis Jackets AB (559489-5301)
**Period:** 2026-01-01 — 2026-03-31
**Wise-wallet:** `1942` (USD)
**FX-rate till SEK:** **9.40**
**Resultat:** 83/83 verifikat klassade, SE balanserar 603 211,43 SEK = 603 211,43 SEK

> Använd den här som mall för **EUR**, **GBP**, **SEK**, **CNY**, **TRY** —
> samma steg, bara byt valuta-argument.

---

## 1. Filer i den här mappen (slutresultat)

| fil | innehåll |
|---|---|
| `statement_107793555_USD_2026-01-01_2026-03-31.csv` | Original-statement från Wise (orörd källa) |
| `usd_brain_dump.txt` | Sami's manuella regler (override för automatik) |
| `WISE_USD_AUDIT.md` | Revisor-MD: alla 83 verifikat grupperade per motkonto + leverantörsgruppering |
| `WISE_USD_STANDALONE.se` | **Visma-redo SIE4-fil** — ladda upp den här |
| `METHODOLOGY_USD.md` | Den här filen |

---

## 2. Klassificeringsregler (priority order)

Skriptet [`analyze_wise_currency.py`](../../../analyze_wise_currency.py) `classify()` kör reglerna i exakt denna ordning — **första träff vinner**:

1. **brain_dump** (`usd_brain_dump.txt`) — Sami's manuella overrides
2. **`future world tech`** → konto **2441** (lev.skuld FWT)
3. **`cashback`** → konto **8311** (ränteintäkt)
4. **FX-konvertering** (`Converted X EUR to Y USD`) → andra Wise-walleten (1943/1944/1945/1940/1949) — INTERNAL, ingen resultatpåverkan
5. **`topped up` / `received money from`** → **1930** (Marginalen företagskonto)
6. **MERCHANT_RULES** — leverantörsmönster (TikTok→5900, GitHub/Cursor/Google Workspace→5420, KLM/Trip/Gotogate→5810, St1/OKQ8/Apcoa→5611, Amazon/Temu/Zalando→4010, …) — **gäller för ALLA valutor**
7. **`card transaction` fallback** → **5460** (förbrukningsmaterial generic) — bara om inget annat matchade

### Bokföringsregel (debet/kredit)

| direction | debet | kredit |
|---|---|---|
| OUT (pengar lämnar Wise) | **motkonto** | **1942** |
| IN (pengar in till Wise) | **1942** | **motkonto** |

---

## 3. Sami's USD-overrides (`usd_brain_dump.txt`)

Beslut tagna 2026-05 efter granskning av merchant-grupperingen i `WISE_USD_AUDIT.md`:

| nyckelord | konto | sida | varför |
|---|---|---|---|
| `4167 kontanten`, `kontanten cityhuset`, `bankomat` | **2893** | PRIVATE | Kontantuttag = privat skuld närstående, **inte** kassa 1910 |
| `klm airline`, `trip.com`, `gotogate` | **2893** | PRIVATE | Privata flygresor — ingen företagsresa |
| `paid to shopify` | **3051** | BUSINESS | Shopify-refund = reverserar försäljning |
| `ahmed gheyath` | **2893** | PRIVATE | Bror, privat |
| `tradera` | **5410** | BUSINESS | Kassasystem + mobil till butik = förbrukningsinventarier |
| `biltema` | **5460** | BUSINESS | Butiksmaterial |

---

## 4. Konton som rörs (slutresultat USD Q1 2026)

| konto | namn | antal | typ |
|---|---|---:|---|
| 1930 | Marginalen företagskonto | (top-ups) | bank |
| 1942 | Wise USD | – | wallet (självkrediteras/debiteras vid alla rader) |
| 1943 | Wise GBP | 1 | INTERNAL FX |
| 1944 | Wise EUR | 13 | INTERNAL FX |
| 1945 | Wise SEK | 4 | INTERNAL FX |
| 2441 | Future World Tech | 5 | leverantörsskuld |
| 2893 | Privata uttag | (8) | privat skuld närstående |
| 3051 | Försäljning 25% | 2 | refund |
| 4010 | Inköp varor | (12) | varukostnad |
| 5410 | Förbrukningsinventarier | (4) | tradera kassa+mobil |
| 5420 | SaaS/programvara | 12 | Cursor, GitHub, Google Workspace, Expo, Shopify-prenumeration |
| 5460 | Förbrukningsmaterial | (2) | Biltema |
| 5611 | Drivmedel/Parkering | 10 | St1, OKQ8, Apcoa |
| 5700 | Frakt | 1 | Shipit |
| 5800 | Resor | 1 | Sörmlandstrafiken |
| 5900 | Reklam | 4 | TikTok Ads |
| 6500 | Övriga kostnader | 2 | Kl Bistro, anmälningsavgift |
| 8311 | Ränteintäkter | 3 | Wise cashback |

> Inga 1910 (kassa), inga 5810 (flyg) — flyttade till **2893** enligt Sami's beslut.

---

## 5. Steg-för-steg: hur jag gjorde det

### Steg 1 — Lägg in CSV
Lägg `statement_*.csv` från Wise i `source_csv/wise/<ccy>/`.

### Steg 2 — Kör analyzer
```powershell
cd Q1_2026_PERIOD_2026-01_TO_2026-03
..\.venv\Scripts\python.exe analyze_wise_currency.py usd
```
Genererar `WISE_USD_AUDIT.md` + `WISE_USD_STANDALONE.se`. Om det finns okända transaktioner skapas även `UNKNOWN_USD.txt`.

### Steg 3 — Granska MD
Öppna `WISE_USD_AUDIT.md`, läs sektion-per-konto. Speciellt **leverantörsgrupperingen** under varje konto — där upptäcker man felklassningar (t.ex. "den här hör inte hemma på 5460").

### Steg 4 — Skriv overrides
För varje felklassad rad, lägg till en regel i `usd_brain_dump.txt`:
```
nyckelord  ->  KONTO  BUSINESS|PRIVATE  fri kommentar
```
Exempel: `klm airline -> 2893 PRIVATE privat flygresa`

### Steg 5 — Kör om
```powershell
..\.venv\Scripts\python.exe analyze_wise_currency.py usd
```
Brain_dump kör först → reglerna applicerar omedelbart. Iterera tills MD ser rätt ut.

### Steg 6 — Verifiera SE balanserar
```powershell
..\.venv\Scripts\python.exe check_se_balance.py "source_csv\wise\usd\WISE_USD_STANDALONE.se"
```
Förväntat: `DEB: 603,211.43  CRED: 603,211.43  diff: 0.00  VER: 83`

### Steg 7 — Ladda upp till Visma
- Visma → Importera → SIE4
- Välj `WISE_USD_STANDALONE.se`
- Periodkontroll: 2026-01-01 — 2026-03-31, RAR 0
- Bekräfta att alla 83 VER importeras

---

## 6. Referenser till regelverk

- [`master-branch/accounting_rules/CASH_AND_COMPANY_ACCOUNT_INSTRUCTIONS.md`](../../../../master-branch/accounting_rules/CASH_AND_COMPANY_ACCOUNT_INSTRUCTIONS.md) – 2893-regel för närstående
- [`master-branch/accounting_rules/MULTI_CURRENCY_ACCOUNTING_PLAN_VIP.md`](../../../../master-branch/accounting_rules/MULTI_CURRENCY_ACCOUNTING_PLAN_VIP.md) – Wise wallet-mappning per valuta
- [`master-branch/accounting_rules/account_list_AI_allowed_UPDATED.txt`](../../../../master-branch/accounting_rules/account_list_AI_allowed_UPDATED.txt) – tillåtna BAS-konton (1946/1582/8310 är förbjudna)

---

## 7. Mall för nästa valuta (EUR/GBP/SEK/CNY/TRY)

1. Lägg `statement_*.csv` i `source_csv/wise/eur/` (eller motsvarande)
2. Kör `..\.venv\Scripts\python.exe analyze_wise_currency.py eur`
3. Öppna `WISE_EUR_AUDIT.md`, granska
4. Lägg overrides i `eur_brain_dump.txt`
5. Kör om → `check_se_balance.py "source_csv\wise\eur\WISE_EUR_STANDALONE.se"`
6. Skapa `METHODOLOGY_EUR.md` (kopiera den här, byt USD→EUR)
7. Ladda upp `.se` till Visma

**Den enda manuella delen är steg 3+4** — granska + skriva brain_dump-regler.
Allt annat är 2 kommandon.
