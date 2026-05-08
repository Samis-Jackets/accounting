# SALES + VAT + COGS — FULL AUDIT Q1 2026 (v3 — moms-dubblering fixad)

## Arkitektur (KORREKT)

Bank-SE-filerna bokar sales NETTO + moms separat:

```
Bank  D brutto
3001  K netto (80 % av brutto)
2611  K moms  (20 % av brutto)
```

→ `2611` är **redan korrekt** efter bank-import. Ingen ytterligare momsextraktion sker.
→ Denna fil bokar **enbart COGS**: `4010 D / 1460 K` = 93 % × netto-25%-sales per månad.

## Moms 2611 per källfil (redan bokat av bank-SE)

| Källa | 2611-summa (kredit−) |
|---|--:|
| LUNAR_STANDALONE.se |     -18,621.66 |
| WISE_EUR_STANDALONE.se |      -5,939.78 |
| WISE_USD_STANDALONE.se |         230.99 |
| WORLDLINE_STANDALONE.se |     -36,332.69 |
| **Σ utgående moms 2611** | **    -60,663.14** |
| **Att betala till SKV (positiv = skuld)** | **     60,663.14** |

## Sales NETTO per månad/konto/källa

| Månad | Konto | Källa | Netto SEK |
|---|---|---|--:|
| 2026-01 | 3001 | LUNAR_STANDALONE.se |    23,912.00 |
| 2026-01 | 3001 | WISE_EUR_STANDALONE.se |    18,071.79 |
| 2026-01 | 3001 | WISE_USD_STANDALONE.se |      -442.25 |
| 2026-01 | 3051 | WORLDLINE_STANDALONE.se |    54,297.15 |
| 2026-01 | 3994 | MARGINALEN_STANDALONE.se |     1,294.00 |
| 2026-02 | 3001 | LUNAR_STANDALONE.se |    22,490.40 |
| 2026-02 | 3001 | WISE_EUR_STANDALONE.se |     5,687.32 |
| 2026-02 | 3001 | WISE_USD_STANDALONE.se |      -481.73 |
| 2026-02 | 3051 | WORLDLINE_STANDALONE.se |    32,875.20 |
| 2026-02 | 3105 | MARGINALEN_STANDALONE.se |    58,000.00 |
| 2026-02 | 3190 | WISE_EUR_STANDALONE.se |     2,839.35 |
| 2026-02 | 3994 | MARGINALEN_STANDALONE.se |    48,374.00 |
| 2026-03 | 3001 | LUNAR_STANDALONE.se |    28,084.25 |
| 2026-03 | 3051 | WORLDLINE_STANDALONE.se |    58,158.40 |

## COGS-kalkyl

| Månad | Netto 25% sales | COGS 93% |
|---|--:|--:|
| 2026-01 | 95,838.69 | 89,129.98 |
| 2026-02 | 60,571.19 | 56,331.21 |
| 2026-03 | 86,242.65 | 80,205.66 |
| **Σ** | **242,652.53** | **225,666.85** |

## Slutsiffror Q1 2026

| Post | SEK |
|---|--:|
| Netto sales 25 % (3001+3051) | 242,652.53 |
| Sales 0 % utland (3105+3190) | 60,839.35 |
| Försäkringsersättning (3994 — separat) | 49,668.00 |
| **Total intäkter (sales+försäkring)** | **353,159.88** |
| Utgående moms 2611 (skuld till SKV) | 60,663.14 |
| KSV 4110 (93 % × netto-25%) | 305,666.85 |
| Bruttomarginal (netto-25% − KSV) | -63,014.32 |

