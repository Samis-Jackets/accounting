# 📂 sales_data — Audit Q1 2026 (Samis Jackets AB)

**Period:** 2026-01-01 → 2026-03-31  |  **Genererad:** 2026-04-29
**Föreslaget bankkonto:**  ()

## 1. Källfiler i denna mapp

Följande råfiler från banken låg i denna mapp och bearbetades av `build_audit_csv.py`. Räkna gärna manuellt i CSV:erna och jämför kolumnen *Rader i råfilen* mot *Inlästa transaktioner*.

| Råfil | Rader i råfilen (datalinjer) | Inlästa transaktioner |
|---|---:|---:|
| AUDIT_sales_data_Q1_2026.csv | 1 | 0 ⚠️ (kontrollera) |
| Lunar export.csv | 273 | 0 ⚠️ (kontrollera) |
| kassa Försäljningsrapport 2026-04-28 14-37.csv | 361 | 1 ⚠️ (kontrollera) |
| **TOTALT** | — | **1** |

> ⚠️ Skillnad i antal raden kan bero på filtrering av rubrik-/summarader. Alla rubrik-/summarader hoppas över medvetet.

## 2. Kontrolltotaler

- **IN (insättningar):** 204 990,00 SEK
- **UT (uttag):** 0,00 SEK
- **Netto perioden:** 204 990,00 SEK
- **Antal needs_review:** 0

## 3. Sammanställning per kategori

| Kategori | Konto(n) | Antal | Summa SEK |
|---|---|---:|---:|
| SALES_SUMMARY | 3051 | 1 | 204 990,00 |

## 4. Sammanställning per BAS-konto (motkonto)

| Konto | Namn | Antal | Summa SEK |
|---|---|---:|---:|
| 3051 | Försäljning Shopify/Swish 25% | 1 | 204 990,00 |

## 5. Alla 1 transaktioner (kronologiskt)

Markera rader med ⚠️ → behöver din bekräftelse innan SE-fil byggs.

| # | Datum | SEK | Original | R | Konto | Kategori | Motpart / Beskrivning | Anledning | ⚠️ |
|---:|---|---:|---:|:---:|:---:|---|---|---|:---:|
| 1 | 2026-03-31 | 204990.00 |  | I | 3051 | SALES_SUMMARY | Kassa POS — Kassa försäljningsrapport - 361 artikelrad… | SUMMERING - matcha mot Marginalen/Worldline/… |  |

---
_Genererad av `build_per_bank_audit.py` från `AUDIT_Q1_2026_FILL_REASONS.csv`._