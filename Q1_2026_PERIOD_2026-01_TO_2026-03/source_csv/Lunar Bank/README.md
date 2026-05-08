# Lunar Bank – metodik

Bankkonto i BAS: **1948**  Valuta: **SEK**

> Lunar SEK-konto. **Första landings-konto för Swish + Stripe-payout (SE-kunder).**

## Huvudreferens
- `..\..\SALES_AND_VAT_METHODOLOGY.md` ⭐ **läs först** – sales/moms-logik
- `..\..\METHODOLOGY.md` (full metodik)

## Försäljning B2C 25 % (det viktigaste)
Alla inkommande Swish-betalningar och Stripe-payouts från SE-kunder är försäljning.
**Brutto bokas på 1948**, krediten splittas auto i:
- **3001** Försäljning varor 25 % SE  (= brutto / 1.25)
- **2611** Utgående moms 25 %  (= brutto − netto)

```
#TRANS 1948 {}  brutto       (debet bank)
#TRANS 3001 {} -netto         (kredit försäljning)
#TRANS 2611 {} -moms          (kredit utgående moms)
```

## Intern transfer (INTE försäljning)
- Lunar → Wise SEK / Marginalen: motkonto = 1945 / 1930. Ingen moms.

## Kontant / privat
- Bankomat/Kontanten/ATM → **2893** (INTE 1910)
- KLM/Trip/Gotogate privatresor → **2893**

## SEK-konvertering
För icke-SEK-rader: `#TRANS`-belopp i SEK, prefix `[orig CCY @ rate = SEK]` i verifikat-noten.
