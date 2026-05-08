# marginalen – metodik

Bankkonto i BAS: **1930**  Valuta: **SEK**

> Företagskonto SEK – ingen FX-konvertering behövs

## Huvudreferens
- `..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik
- `..\..\METHODOLOGY.md` (full metodik)

## Försäljning B2C 25 % (faktura-betalningar)
Fakturor (BG-inbetalningar) från SE-kunder bokas:
- **1930** debet (brutto in)
- **3001** kredit (netto = brutto/1.25)
- **2611** kredit (moms = brutto − netto)

## Intern transfer (INTE försäljning)
- Marginalen ↔ Lunar / Wise SEK / Worldline-payout: motkonto = motsvarande 19xx. Ingen moms.

## Kontant / privat
- Bankomat/Kontanten/ATM → **2893** (INTE 1910)
- KLM/Trip/Gotogate privatresor → **2893**

## SEK-konvertering
För icke-SEK-rader: `#TRANS`-belopp i SEK, prefix `[orig CCY @ rate = SEK]` i verifikat-noten.
