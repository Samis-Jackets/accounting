# Worldline – metodik

Bankkonto i BAS: **1947**  Valuta: **SEK**

> Kortinlösen-payout. **Första landings-konto för fysisk butik kortbetalning.**

## Huvudreferens
- `..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik
- `..\..\METHODOLOGY.md` (full metodik)

## Försäljning B2C 25 % + Worldline-avgift
Kortbetalningar i butiken landar som payout i 1947. Brutto-belopp i payouten
splittas i netto + moms; eventuell separat avgift bokas på 6570.

```
#TRANS 1947 {}  brutto-payout           (debet bank)
#TRANS 3001 {} -netto                    (kredit försäljning 25 % SE)
#TRANS 2611 {} -moms                     (kredit utgående moms)
#TRANS 6570 {}  worldline-avgift         (debet kortavgift, om separat rad)
#TRANS 1947 {} -worldline-avgift         (kredit bank för avgiften)
```

> Om Worldline drar avgiften från payouten direkt, redovisa **bruttoförsäljning =
> payout + avgift** för att momsen ska bli rätt.

## Intern transfer (INTE försäljning)
- Worldline → Marginalen utbetalning: motkonto = 1930. Ingen moms.

## Kontant / privat
- Bankomat/Kontanten/ATM → **2893** (INTE 1910)

## SEK-konvertering
För icke-SEK-rader: `#TRANS`-belopp i SEK, prefix `[orig CCY @ rate = SEK]` i verifikat-noten.
