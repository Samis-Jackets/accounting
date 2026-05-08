# 🔍 ACCOUNT 2893 ANALYSIS - Q1 2026
## Complete Analysis of All Transactions with "Skulder till närstående personer"

**Account:** 2893 - Skulder till närstående personer, kortfristig del (Debt to Related Persons)  
**Period:** 2026-01-01 to 2026-03-31  
**Opening Balance:** -1,598,927.35 SEK (You are OWED this by the company)  
**Closing Balance:** -1,680,176.56 SEK (You are OWED this by the company)  
**Net Change:** -81,249.21 SEK (Company owes you MORE)

---

## 📊 TRANSACTION SUMMARY

### Total Movements:
- **Money you LOANED to company:** 95,305.40 SEK ↓ (You put money IN)
- **Money company PAID BACK to you:** 14,056.19 SEK ↑ (You took money OUT or company paid expenses)

**Net effect:** You loaned the company 81,249.21 SEK MORE than you got back.

---

## 💰 KEY WISE EUR TRANSACTION - A391

### ✅ **CORRECT ENTRY:**
```
#VER A 391 20260306 "Received money from MOHAMMAD SAMI ALSHAR [WISE_EUR]"
{
   #TRANS 1944 {} 33609.03      // DEBIT: Wise EUR bank increases
   #TRANS 2893 {} -33609.03     // CREDIT: Debt to you increases (company owes you more)
}
```

### 🎯 **WHY THIS IS CORRECT:**

**What happened:** You (Mohammad Sami Alsharef) transferred 2,974.25 EUR (= 33,609.03 SEK) TO the company's Wise EUR account.

**Accounting treatment:**
1. **Bank account (1944) INCREASES** by 33,609.03 SEK
   - Direction: DEBIT (positive number)
   - Effect: Company has MORE money in Wise EUR

2. **Debt to you (2893) INCREASES** by 33,609.03 SEK
   - Direction: CREDIT (negative number in SIE)
   - Effect: Company owes you MORE money
   - This is a LIABILITY (debt the company must repay)

**In accounting:**
- Assets INCREASE = DEBIT (positive)
- Liabilities INCREASE = CREDIT (negative)

---

## 📋 ALL WISE EUR TRANSACTIONS WITH YOU (2893)

| Date | Ver | Description | Amount SEK | Direction | Your Debt Balance |
|------|-----|-------------|----------:|-----------|------------------:|
| **06-03** | A 391 | **You LOANED money to company** | **+33,609.03** | **IN** | **Increases debt to you** |
| 09-03 | A 415 | Company PAID YOU BACK | -11,300.00 | OUT | Reduces debt to you |
| 10-03 | A 417 | You paid KLM ticket (company owes you) | +416.29 | Your expense | Increases debt to you |
| 10-03 | A 418 | You paid KLM ticket (company owes you) | +1,777.15 | Your expense | Increases debt to you |
| 12-03 | A 420 | You used card at Kontanten | +1,639.52 | Your expense | Increases debt to you |
| 24-03 | A 462 | You used card at Lidl | +713.26 | Your expense | Increases debt to you |

**Net from Wise EUR:** +26,855.25 SEK (Company owes you this much MORE from these transactions)

---

## 🔄 ALL TRANSACTIONS WITH ACCOUNT 2893 IN Q1 2026

### Money you LOANED to company (Credits to 2893):

| Ver | Date | Source | Amount | Description |
|-----|------|--------|-------:|-------------|
| A 391 | 06-03 | **WISE_EUR** | **33,609.03** | **Your transfer to company** |
| A 240 | 04-02 | WISE_USD | 6,862.28 | Your expense |
| A 249 | 04-02 | WISE_USD | 1,524.96 | Your expense |
| A 388 | 05-03 | WISE_USD | 1,184.40 | Your card expense |
| ... | ... | ... | ... | (Many more card transactions) |

**Total loaned:** 95,305.40 SEK

### Money company PAID BACK or you withdrew (Debits to 2893):

| Ver | Date | Source | Amount | Description |
|-----|------|--------|-------:|-------------|
| A 415 | 09-03 | **WISE_EUR** | **11,300.00** | **Company paid you back** |
| A 162 | 27-01 | MARGINALEN | 3,000.00 | Repayment |
| A 173 | 28-01 | LUNAR | 2,740.00 | Repayment |
| ... | ... | ... | ... | (More repayments) |

**Total paid back:** 14,056.19 SEK

---

## ✅ VERIFICATION: A391 IS CORRECT

### The Entry:
```
#VER A 391 20260306 "Received money from MOHAMMAD SAMI ALSHAR [WISE_EUR]"
{
   #TRANS 1944 {} 33609.03      // ✅ Bank increases (asset UP)
   #TRANS 2893 {} -33609.03     // ✅ Debt to you increases (liability UP)
}
```

### Why the negative sign on 2893?

**Account 2893 is a LIABILITY account** (debt the company owes to you).

In SIE4 format:
- **CREDIT = NEGATIVE number** (increases liability)
- **DEBIT = POSITIVE number** (decreases liability)

So when you loan money TO the company:
- Your debt account gets a CREDIT entry = -33,609.03
- This INCREASES the amount the company owes you

---

## 🎯 WHAT THIS MEANS

### Current Status:
- **Opening balance:** -1,598,927.35 SEK (Company owed you this at start of Q1)
- **You loaned MORE:** -81,249.21 SEK (Net increase in Q1)
- **Closing balance:** -1,680,176.56 SEK (Company owes you this at end of Q1)

### The A391 transaction:
- ✅ **CORRECT** - You put 33,609.03 SEK into the company
- ✅ **CORRECT** - Company now owes you 33,609.03 SEK MORE
- ✅ **CORRECT** - Bank account (1944) increased
- ✅ **CORRECT** - Debt to you (2893) increased

---

## ❌ WHAT WOULD BE WRONG

### If the entry was like this (WRONG):
```
#VER A 391 20260306 "Received money from MOHAMMAD SAMI ALSHAR [WISE_EUR]"
{
   #TRANS 1944 {} 33609.03      // Bank increases
   #TRANS 2893 {} 33609.03      // ❌ WRONG - This would REDUCE debt to you
}
```

**This would be WRONG because:**
- It would make it look like you're being PAID BACK 33,609.03
- But actually you're GIVING money to the company
- The debt to you should INCREASE, not decrease

---

## 📝 CONCLUSION

### ✅ The current entry (A391) is **CORRECT**

**Logic:**
1. You transferred money FROM your personal account TO the company's Wise EUR
2. This is a LOAN from you to the company
3. Bank account (1944 Wise EUR) goes UP → DEBIT (positive)
4. Debt to you (2893) goes UP → CREDIT (negative)

### The accounting is CORRECT, NOT dangerous.

**The negative sign means:** "Company owes you MORE money (liability increases)"  
**NOT:** "You're taking money out"

---

## 🔧 IF YOU WANT TO CHANGE IT

If you believe the DIRECTION is wrong (i.e., you actually WITHDREW money instead of loaning it), then you need to:

1. **Reverse the entry** (make bank decrease, debt to you decrease)
2. **Find the matching expense** where this money went

**But based on the Wise EUR statement, this shows as:**
- **"Received money from MOHAMMAD SAMI ALSHAREF"** 
- Direction: **IN** (money came INTO the company)
- This is a LOAN from you to company ✅

---

**Status:** ✅ CORRECT ACCOUNTING  
**Date analyzed:** 2026-05-07  
**Source data:** MASTER_Q1_2026_CORRECTED_CASH_BASIS.se, WISE_EUR_STANDALONE.se, WISE_EUR_AUDIT.md
