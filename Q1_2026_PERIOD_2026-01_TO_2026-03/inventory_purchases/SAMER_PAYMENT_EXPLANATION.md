# 💰 SAMER ALSHAREF PAYMENT TO FUTURE WORLD TECH
## Loan Transaction - 373,303 SEK

---

## 📋 TRANSACTION DETAILS

| Item | Amount |
|------|-------:|
| **Amount (SEK)** | 373,303.00 |
| **Amount (USD)** | ~38,885 USD @ 9.6 |
| **Paid by** | Mr. Mhd Samer Alsharef |
| **Paid to** | Future World Tech (China) |
| **Date** | 2026-03-31 |

---

## 💡 WHAT HAPPENED?

Samer Alsharef paid Future World Tech in China **on behalf of Samis Jackets AB**.

This creates a **loan from Samer to the company** that must be repaid later.

---

## 💳 SIE4 ENTRY

```
#VER A 528 20260331 "Payment to FWT by Samer Alsharef - 373,303 SEK (38,885 USD @ 9.6)"
{
   #TRANS 2441 {} 373303.00 20260331 "Paid to Future World Tech in China by Samer"
   #TRANS 2893 {} -373303.00 20260331 "Loan from Mhd Samer Alsharef - 38,885 USD"
}
```

---

## 📊 ACCOUNT MOVEMENTS

| Account | Name | Change | Effect |
|---------|------|-------:|--------|
| **2441** | Leverantörsskulder (FWT) | **+373,303** | ⬇️ **Reduces** debt to Future World Tech |
| **2893** | Skulder till närstående | **-373,303** | ⬆️ **Increases** debt to Samer Alsharef |

---

## 🔄 BALANCE IMPACT

### Account 2441 (Future World Tech Supplier Debt):
```
Before:  1,828,375.01 SEK (after FWT invoice)
- Samer payment: -373,303.00 SEK
────────────────────────
After:   1,455,072.01 SEK (remaining debt to FWT)
```

### Account 2893 (Debt to Samer Alsharef):
```
Before:  (unknown) SEK
+ Samer loan: +373,303.00 SEK
────────────────────────
After:   373,303.00 SEK (debt owed to Samer - must repay)
```

---

## ✅ BALANCE VERIFICATION

**Debits:**  373,303.00 SEK (Account 2441)  
**Credits:** 373,303.00 SEK (Account 2893)  
✅ **BALANCED**

---

## 💡 WHY THIS ENTRY?

1. **Samer paid FWT in China** → This reduces company's debt to FWT (debit 2441)
2. **Company now owes Samer** → This creates debt to Samer (credit 2893)
3. **Must repay Samer later** → Account 2893 tracks how much we owe him

---

## 📝 NOTE: USD CONVERSION

- **SEK:** 373,303.00
- **USD:** ~38,885 USD (at exchange rate 9.6)
- **Calculation:** 373,303 ÷ 9.6 = 38,885.73 USD

The USD amount is shown in the transaction note for reference.

---

## 📁 FILES

- **SAMER_PAYMENT_FWT_STANDALONE.se** - Standalone SIE file ready for Visma import

---

## ✅ READY TO IMPORT

**File:** SAMER_PAYMENT_FWT_STANDALONE.se  
**Verification:** A 528  
**Date:** 2026-03-31  
**Amount:** 373,303 SEK  

---

**Status:** ✅ READY FOR VISMA IMPORT  
**Type:** Loan transaction (Samer → Company)  
**Purpose:** Payment to Future World Tech in China
