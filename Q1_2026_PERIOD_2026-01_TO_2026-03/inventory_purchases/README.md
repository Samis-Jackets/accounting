# 📦 Future World Tech Invoice Processing

**Invoice:** FWT-SJ-2026-Q1-001  
**Amount:** $126,882.90 USD @ 9.6 = 1,218,075.84 SEK  
**Import VAT 25%:** 304,518.96 SEK (reverse charge)  
**Total Debits:** 1,522,594.80 SEK (~1.5M)  
**Units:** 49,548 items across 27 products

**Samer Payment:** 373,303 SEK (~38,885 USD) paid to FWT in China

---

## 🚨 TWO SEPARATE TRANSACTIONS

### Transaction 1: FWT Invoice (with reverse charge VAT)
- **File:** FWT_INVOICE_STANDALONE.se
- **Entry:** A 526
- **Purpose:** Record invoice from Future World Tech

### Transaction 2: Samer Payment to FWT
- **File:** SAMER_PAYMENT_FWT_STANDALONE.se
- **Entry:** A 528
- **Purpose:** Record payment made by Samer Alsharef in China

---

## ⭐ QUICK START

### FWT Invoice Entry:
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

### Samer Payment Entry:
```
#VER A 528 20260331 "Payment to FWT by Samer Alsharef - 373,303 SEK (38,885 USD @ 9.6)"
{
   #TRANS 2441 {} 373303.00
   #TRANS 2893 {} -373303.00
}
```

---

## 💡 WHY 1.5 MILLION INSTEAD OF 1.2 MILLION?

| Component | Amount (SEK) |
|-----------|-------------:|
| Invoice amount | 1,218,075.84 |
| Import VAT 25% | 304,518.96 |
| **Total debits** | **1,522,594.80** (~1.5M) |

**The difference is the reverse charge VAT:**
- Account 2645: -304,518.96 SEK (VAT you can reclaim)
- Account 2615: +304,518.96 SEK (VAT you owe to government)
- **These cancel out** in the quarterly VAT return

---

## 📊 COMBINED ACCOUNT 2441 BALANCE

| Step | Transaction | Change | Balance |
|------|-------------|-------:|--------:|
| Opening | Q1 start | - | 610,300.17 |
| + Invoice | FWT Invoice (A 526) | +1,218,075.84 | 1,828,375.01 |
| - Payment | Samer Payment (A 528) | -373,303.00 | **1,455,072.01** |

**Final debt to Future World Tech:** 1,455,072.01 SEK (~1.46M)

---

## 📊 NEW DEBT TO SAMER (ACCOUNT 2893)

| Transaction | Amount |
|-------------|-------:|
| Samer paid FWT in China | 373,303.00 SEK |
| **Total owed to Samer** | **373,303.00 SEK** |

This must be repaid to Samer Alsharef later.

---

## 📄 FILES

### FWT Invoice Files:
1. **FWT_INVOICE_STANDALONE.se** ⭐ **VISMA IMPORT FILE**
   - Invoice with reverse charge VAT
   - Entry A 526

2. **FINAL_ENTRY.txt**
   - Copy-paste ready entry
   - Balance explanation

### Samer Payment Files:
3. **SAMER_PAYMENT_FWT_STANDALONE.se** ⭐ **VISMA IMPORT FILE**
   - Payment made by Samer in China
   - Entry A 528

4. **SAMER_PAYMENT_EXPLANATION.md**
   - Complete explanation
   - Account balance calculations

### Supporting Files:
5. **CORRECTED_INVENTORY_DATABASE.csv**
   - Product database (27 SKUs)

6. **IMPORT_VAT_ENTRIES.md**
   - Reverse charge VAT explanation

---

## 📊 ACCOUNT BREAKDOWN

| Account | Category | Amount (SEK) |
|---------|----------|-------------:|
| **1460** | Inventory (resale) | 791,575.22 |
| **5460** | Packaging | 183,926.02 |
| **1220** | Equipment | 242,574.60 |
| **2441** | Supplier debt (credit) | -1,218,075.84 |
| **2645** | Import VAT (debit) | 304,518.96 |
| **2615** | Reverse charge VAT (credit) | -304,518.96 |
| **TOTAL** | | **0.00** ✅ |

---

## 💡 REVERSE CHARGE VAT EXPLAINED

**Why do we add VAT if it cancels out?**

Swedish tax law requires you to:
1. Charge yourself 25% VAT on imports (2615 - utgående moms)
2. Can immediately reclaim that 25% VAT (2645 - ingående moms)
3. Report both in quarterly VAT return
4. Net effect = 0 SEK to pay

**This is called "reverse charge" or "omvänd skattskyldighet"**

---

## 📈 WHY ACCOUNT 2441 SHOWS 1.8M

After this entry, account 2441 (Supplier debt to FWT) will show:

```
Opening:  610,300.17 SEK (existing debt from previous invoices)
+ Invoice: 1,218,075.84 SEK (this invoice)
──────────────────────
Total:   1,828,375.01 SEK (~1.8M total debt to Future World Tech)
```

This is normal - it's the cumulative debt to the supplier.  
Payments are handled separately through Worldline account.

---

## ✅ NEXT STEPS

1. ✅ Import **FWT_INVOICE_STANDALONE.se** (Entry A 526)
   - Records invoice with reverse charge VAT
   - Increases account 2441 by 1,218,075.84 SEK

2. ✅ Import **SAMER_PAYMENT_FWT_STANDALONE.se** (Entry A 528)
   - Records Samer's payment to FWT in China
   - Reduces account 2441 by 373,303.00 SEK
   - Creates debt to Samer (account 2893)

3. ✅ Verify balances:
   - Account 2441: Should be 1,455,072.01 SEK
   - Account 2893: Should be 373,303.00 SEK

4. ✅ Include in Q1 2026 quarterly VAT return

5. ✅ **Remember to repay Samer Alsharef later** (373,303 SEK)

---

## 📚 REFERENCE

**Pattern from 2025 SE file:**
```
#VER A 588 20250228 "First China container"
{
   #TRANS 2441 {} -368492.00
   #TRANS 4545 {} 368492.00
   #TRANS 2645 {} -92123.00
   #TRANS 2615 {} 92123.00
}
```

Same pattern, just with multiple asset accounts.

---

**Last Updated:** 2026-05-07  
**Status:** ✅ TWO TRANSACTIONS READY  
**Transaction 1:** FWT Invoice (A 526) - 1.2M + 0.3M VAT  
**Transaction 2:** Samer Payment (A 528) - 373K loan  
**Net debt to FWT:** 1.46M SEK  
**Debt to Samer:** 373K SEK (must repay)
