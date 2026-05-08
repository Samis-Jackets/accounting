# ✅ FINAL CORRECTED - SIMPLE INVOICE ENTRY
## Invoice: $126,882.90 USD × 9.6 = 1,218,075.84 SEK

---

## 📋 THE SIMPLE TRUTH

| Item | Amount |
|------|-------:|
| **Invoice (USD)** | $126,882.90 |
| **Exchange Rate** | 9.6 SEK/USD |
| **Invoice (SEK)** | **1,218,075.84 SEK** |
| **VAT 25%** | **304,518.96 SEK** |
| **Total Payment** | **1,522,594.80 SEK** |

**NO freight, NO customs, NO extra costs. This is it.**

---

## 📦 ACCOUNT ALLOCATION (Approximate)

Based on invoice content (27 products, 49,548 units):

| Account | Category | Approx SEK | % |
|---------|----------|----------:|---:|
| **1460** | Inventory (resale) | 792,000 | 65% |
| **5460** | Packaging | 184,000 | 15% |
| **1220** | Equipment | 242,076 | 20% |
| **TOTAL** | | **1,218,075.84** | 100% |

**Note:** Exact product-level breakdown available in CORRECTED_SIMPLE_INVOICE_PROCESSING.md

---

## 💳 SIE4 ENTRY (COPY-PASTE READY)

**Update: verification number (A 526) and date (20260320)**

```
#VER A 526 20260320 "Varuinköp FWT - $126,882.90 @ 9.6 [WISE USD]"
{
   #TRANS 1460 {} 792000.00
   #TRANS 5460 {} 184000.00
   #TRANS 1220 {} 242075.84
   #TRANS 2641 {} 304518.96
   #TRANS 1942 {} -1522594.80
}
```

**Balance check:**  
Debits: 792,000.00 + 184,000.00 + 242,075.84 + 304,518.96 = **1,522,594.80**  
Credits: 1,522,594.80  
✅ **BALANCED**

---

## 🔄 VAT BOTH SIDES

### When BUYING (Ingående moms - Account 2641):
```
#TRANS 2641 {} 304518.96    // Input VAT - deductible
```
→ You reclaim this from Skatteverket

### When SELLING (Utgående moms - Account 2611):
```
#TRANS 2611 {} -XXX.XX      // Output VAT - charged to customer
```
→ You pay this to Skatteverket

**Example sale: 100 rings @ 50 SEK each retail:**
```
#VER A XXX 20260425 "Försäljning ringar - 100 st"
{
   #TRANS 1940 {} 6250.00
   #TRANS 3051 {} -5000.00
   #TRANS 2611 {} -1250.00
}
```

**VAT net:**
- Input VAT: +304,518.96 SEK (from purchase)
- Output VAT: -1,250.00 SEK (from sale)
- Net to reclaim: 303,268.96 SEK

---

## 📊 ACCOUNT BALANCES AFTER

| Account | Before | Change | After |
|---------|-------:|-------:|------:|
| **1460** | 566,933.00 | +792,000.00 | 1,358,933.00 |
| **1220** | 49,170.68 | +242,075.84 | 291,246.52 |
| **5460** | (varies) | +184,000.00 | (varies) |
| **2641** | 1,053.60 | +304,518.96 | 305,572.56 |
| **1942** | 4,503.41 | -1,522,594.80 | -1,518,091.39 |

---

## ✅ CHECKLIST

Before SIE:
- [ ] Invoice: $126,882.90 USD
- [ ] Rate: 9.6 SEK/USD
- [ ] Total SEK: 1,218,075.84 (EXACT)
- [ ] VAT 25%: 304,518.96
- [ ] Payment: 1,522,594.80 SEK
- [ ] Date from Wise USD statement

After SIE:
- [ ] Entry balanced
- [ ] Accounts updated
- [ ] VAT 2641 to reclaim

---

## 🚨 RULES

✅ Invoice price ONLY  
✅ NO additions  
✅ ONE VAT: 25%  
✅ TWO VAT accounts: 2641 (in) + 2611 (out)  
✅ Cash basis: when paid  
✅ Historical accounts: 1460, 1220, 5460

---

**Ready to add to MASTER_Q1_2026_CORRECTED_CASH_BASIS.se**
