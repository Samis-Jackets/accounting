# ✅ IMPORT VAT ENTRIES - FUTURE WORLD TECH INVOICE
## Reverse Charge Mechanism for China Imports

---

## 📚 PATTERN FROM 2025 SE FILE

Looking at how imports were handled in 2025, the pattern is:

1. **Invoice Entry**: Record goods + reverse charge VAT (2645/2615)
2. **Payment Entry**: Pay supplier from Wise USD
3. **VAT Reporting Entry**: Clear reverse charge in quarterly VAT return

---

## 💳 ENTRY 1: INVOICE WITH REVERSE CHARGE VAT

**Date:** 2026-03-31 (invoice date)  
**Purpose:** Record inventory purchase + import VAT liability

```
#VER A 526 20260331 "FWT Invoice FWT-SJ-2026-Q1-001 - $126,882.90 @ 9.6"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2441 {} -1218075.84
   #TRANS 2645 {} -304518.96
   #TRANS 2615 {} 304518.96
}
```

**What this does:**
- Debit 1460/5460/1220: Increase inventory/packaging/equipment
- Credit 2441: Create supplier debt to Future World Tech
- Credit 2645: Record import VAT (can reclaim)
- Debit 2615: Record VAT owed to government (reverse charge)

**Balance check:**
- Debits: 791,575.22 + 183,926.02 + 242,574.60 + 304,518.96 = 1,522,594.80
- Credits: 1,218,075.84 + 304,518.96 = 1,522,594.80
- ✅ BALANCED

---

## 💳 ENTRY 2: PAYMENT TO SUPPLIER

**Date:** 2026-03-20 (payment date from Wise USD)  
**Purpose:** Pay off supplier debt

```
#VER A 527 20260320 "Payment to FUTURE WORLD TECH INTERNAT [WISE_USD]"
{
   #TRANS 2441 {} 1218075.84
   #TRANS 1942 {} -1218075.84
}
```

**What this does:**
- Debit 2441: Reduce supplier debt (pay off what we owe)
- Credit 1942: Reduce Wise USD bank account (money out)

**Balance check:**
- Debits: 1,218,075.84
- Credits: 1,218,075.84
- ✅ BALANCED

---

## 💳 ENTRY 3: VAT REPORTING (Q1 2026)

**Date:** 2026-03-31 (end of quarter)  
**Purpose:** Clear reverse charge VAT in quarterly return

```
#VER A XXX 20260331 "Momsredovisning januari-mars 2026"
{
   #TRANS 2645 {} 304518.96
   #TRANS 2615 {} -304518.96
   #TRANS 2641 {} -[other input VAT]
   #TRANS 2611 {} [other output VAT]
   #TRANS 2650 {} [net to pay/receive from Skatteverket]
}
```

**What this does:**
- Debit 2645: Clear import VAT (move to settlement)
- Credit 2615: Clear output VAT (move to settlement)
- These amounts cancel out in most cases
- Net calculation with other VAT goes to 2650

**Note:** The exact amounts for 2641/2611/2650 depend on other transactions in Q1 2026. This entry combines ALL VAT transactions for the quarter.

---

## 📊 ACCOUNT MOVEMENTS

### After Entry 1 (Invoice):
| Account | Change | New Balance |
|---------|-------:|------------:|
| 1460 | +791,575.22 | 1,358,508.22 |
| 5460 | +183,926.02 | (varies) |
| 1220 | +242,574.60 | 291,745.28 |
| 2441 | -1,218,075.84 | 1,828,375.01 * |
| 2645 | -304,518.96 | (liability) |
| 2615 | +304,518.96 | (liability) |

**\* Account 2441:** Opens at 610,300.17 + 1,218,075.84 = 1,828,375.01

### After Entry 2 (Payment):
| Account | Change | New Balance |
|---------|-------:|------------:|
| 2441 | +1,218,075.84 | 610,300.17 (back to opening) |
| 1942 | -1,218,075.84 | -1,213,572.43 |

### After Entry 3 (VAT Reporting):
| Account | Change | Effect |
|---------|-------:|--------|
| 2645 | +304,518.96 | Clears to zero |
| 2615 | -304,518.96 | Clears to zero |

---

## 🔑 KEY DIFFERENCES FROM SIMPLE ENTRY

**WRONG (Previous - no VAT):**
```
#VER A 526 20260331 "FWT Invoice"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2441 {} -1218075.84
}
```

**CORRECT (This version - with reverse charge VAT):**
```
#VER A 526 20260331 "FWT Invoice"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2441 {} -1218075.84
   #TRANS 2645 {} -304518.96    ← ADDED: Import VAT (can reclaim)
   #TRANS 2615 {} 304518.96     ← ADDED: Output VAT (owe to gov)
}
```

---

## 💡 WHY REVERSE CHARGE?

**From Swedish VAT Law (Mervärdesskattelagen):**

When importing goods from outside EU:
1. You must charge yourself 25% VAT (2615 - utgående moms)
2. You can immediately reclaim that same 25% VAT (2645 - ingående moms)
3. These cancel out in the VAT return (net effect = 0 in most cases)
4. This is called "reverse charge" or "omvänd skattskyldighet"

**Account meanings:**
- **2645**: Beräknad ingående moms på förvärv från utlandet (Calculated input VAT on imports)
- **2615**: Utgående moms, omvänd skattskyldighet (Output VAT, reverse charge)

**Why do this?**
- Swedish tax law requires you to report imports
- But you don't actually pay extra VAT (it cancels out)
- Customs/import duties are separate (not shown here)

---

## ✅ STANDALONE SIE FILE

See **FWT_INVOICE_WITH_VAT_STANDALONE.se** for a complete standalone file with all three entries ready for Visma import.

---

## 📋 COMPARISON WITH 2025 PATTERN

**2025 China Container Invoice (from 20240701-20251231.se):**
```
#VER A 588 20250228 "First China container"
{
   #TRANS 2441 {} -368492.00
   #TRANS 4545 {} 368492.00
   #TRANS 2645 {} -92123.00
   #TRANS 2615 {} 92123.00
}
```

**2026 FWT Invoice (this entry):**
```
#VER A 526 20260331 "FWT Invoice FWT-SJ-2026-Q1-001"
{
   #TRANS 2441 {} -1218075.84
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2645 {} -304518.96
   #TRANS 2615 {} 304518.96
}
```

**Same pattern, just different amounts and multiple asset accounts.**

---

**Status:** ✅ MATCHES 2025 PATTERN  
**Method:** Reverse charge VAT  
**Accounts:** 2645 (import VAT) + 2615 (output VAT)  
**Ready for:** Visma import
