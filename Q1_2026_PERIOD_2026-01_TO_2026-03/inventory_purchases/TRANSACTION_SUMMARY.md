# 📊 SUMMARY - FWT TRANSACTIONS Q1 2026

---

## 🔄 TRANSACTION FLOW

```
┌─────────────────────────────────────────────────────────────┐
│ TRANSACTION 1: FWT INVOICE (A 526)                          │
├─────────────────────────────────────────────────────────────┤
│ Invoice: $126,882.90 USD @ 9.6 = 1,218,075.84 SEK          │
│                                                              │
│ DEBIT:                          CREDIT:                     │
│ 1460: 791,575.22               2441: 1,218,075.84          │
│ 5460: 183,926.02               2615: 304,518.96            │
│ 1220: 242,574.60                                            │
│ 2645: 304,518.96                                            │
│                                                              │
│ Result: Debt to FWT = 1,828,375.01 SEK                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ TRANSACTION 2: SAMER PAYMENT (A 528)                        │
├─────────────────────────────────────────────────────────────┤
│ Payment: 373,303 SEK (~38,885 USD @ 9.6)                   │
│                                                              │
│ DEBIT:                          CREDIT:                     │
│ 2441: 373,303.00               2893: 373,303.00            │
│                                                              │
│ Result: Debt to FWT reduced by 373,303 SEK                 │
│         Debt to Samer created: 373,303 SEK                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 FINAL BALANCES

### Account 2441 (Leverantörsskulder - Future World Tech):
```
Opening:         610,300.17 SEK
+ Invoice:     1,218,075.84 SEK
- Samer pay:    -373,303.00 SEK
────────────────────────────────
FINAL:         1,455,072.01 SEK
```

### Account 2893 (Skulder till närstående - Samer Alsharef):
```
Opening:              0.00 SEK
+ Samer loan:   373,303.00 SEK
────────────────────────────────
FINAL:          373,303.00 SEK  ⚠️ MUST REPAY
```

---

## 💰 WHAT DOES THIS MEAN?

1. **Future World Tech Invoice:** 1.2M SEK
   - Inventory: 791K
   - Packaging: 184K
   - Equipment: 243K
   - VAT (reverse charge): 305K

2. **Samer paid FWT:** 373K SEK in China
   - Reduced company debt to FWT
   - Created debt to Samer (must repay)

3. **Net result:**
   - Still owe FWT: 1.46M SEK
   - Owe Samer: 373K SEK
   - Total liabilities: 1.83M SEK

---

## 📋 IMPORT ORDER

1. **First:** FWT_INVOICE_STANDALONE.se (A 526)
2. **Second:** SAMER_PAYMENT_FWT_STANDALONE.se (A 528)

---

## ✅ CHECKLIST

- [ ] Import FWT Invoice (A 526)
- [ ] Import Samer Payment (A 528)
- [ ] Verify account 2441 = 1,455,072.01 SEK
- [ ] Verify account 2893 = 373,303.00 SEK
- [ ] Include VAT in Q1 2026 return
- [ ] **Schedule repayment to Samer Alsharef**

---

**Status:** ✅ READY FOR VISMA IMPORT  
**Date:** 2026-03-31  
**Total transactions:** 2
