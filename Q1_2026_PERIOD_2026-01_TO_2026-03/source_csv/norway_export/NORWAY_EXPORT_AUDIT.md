# 🇳🇴 NORGE EXPORT — Q1 2026

> Wholesale-försäljning till Norge (utanför EU). **0 % moms**.
> BAS-konto: **3105 — Försäljning varor till land utanför EU**
> Allt går genom **Marginalen företagskonto (1930)**.

## 📋 Transaktioner Q1 2026

| Datum | Belopp SEK | Bank | Beskrivning | Faktura/Bevis |
|---|--:|---|---|---|
| 2026-02-18 | **+18 000,00** | Marginalen | Mohamad Sharif A Qalaji (kund Norge) | `INVOICE_2026-02-18_Qalaji_18000.pdf` ⏳ |
| 2026-02-19 | **+28 000,00** | Marginalen | CI-2026-001 (Customer Invoice nr 1) | `CI-2026-001.pdf` ⏳ |
| 2026-02-20 | **+12 000,00** | Marginalen | CI-2026-001 (delbetalning eller followup) | `CI-2026-001_part2.pdf` ⏳ |
| **SUMMA SALES** | **+58 000,00** | | | |
| 2026-03-02 | **-5 299,00** | Marginalen | Norge frakt utan moms (kostnad) | `FRAKT_Norge_5299.pdf` ⏳ |
| **NETTO** | **+52 701,00** | | | |

## 🧾 Bokföring

### VER: Mohamad Sharif A Qalaji (2026-02-18)
```
#TRANS 1930  18000.00      ; in på Marginalen
#TRANS 3105 -18000.00      ; export Norge 0% moms
```
✅ INGEN 2611 (export → 0% moms)

### VER: CI-2026-001 (2026-02-19 + 2026-02-20)
```
#TRANS 1930  28000.00 / 12000.00
#TRANS 3105 -28000.00 / -12000.00
```

### VER: Norge frakt (2026-03-02)
```
#TRANS 1930  -5299.00
#TRANS 5710   5299.00
```

## 📂 Bevis-mapp (lägg fakturor här)

```
source_csv/norway_export/invoices/
├── INVOICE_2026-02-18_Qalaji_18000.pdf
├── CI-2026-001.pdf
├── CI-2026-001_part2.pdf
└── FRAKT_Norge_5299.pdf
```

Kör: `Add-Content` eller dra-och-släpp PDF/foton hit.

## ⚖️ Skattemässig hantering

- **Export utanför EU**: 0 % moms enligt ML 5 kap. 3 a § (Mervärdesskattelagen)
- **Bevis krävs**: 
  - Faktura med kundens norska orgnr
  - Transportdokument (Schenker/DSV/PostNord) som visar att varan lämnat Sverige
  - Tullexportdokument (om tullvärde > 1 000 SEK)
- **Moms-deklaration ruta 36**: Försäljning varor till land utanför EU
- **EU-försäljningslista**: Behövs INTE (Norge är EFTA, ej EU)

## 🔍 Avstämning mot Marginalen-CSV

```bash
..\.venv\Scripts\python.exe _find_norway.py
```
Söker efter: `mohamad`, `sharif`, `qalaji`, `ci-`, `norge`, `norway`

## ✅ Status

- [x] Klassificering 3105 i `analyze_bank.py` (export 0%)
- [x] Brain-dump regler för Qalaji + CI-2026-001
- [x] Re-bygg `MARGINALEN_STANDALONE.se` med 3105
- [ ] Lägg fakturor i `invoices/` mapp
- [ ] Verifiera norsk kundens orgnr på Brønnøysundregistrene
- [ ] Lägg in transportdokument
