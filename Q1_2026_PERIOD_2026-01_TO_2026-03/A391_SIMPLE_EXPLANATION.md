# 💡 SIMPLE EXPLANATION - A391 Transaction

## What Happened on 06-03-2026?

**Transaction:** "Received money from MOHAMMAD SAMI ALSHAR [WISE_EUR]"  
**Amount:** 2,974.25 EUR = 33,609.03 SEK  
**Direction:** Money came INTO Wise EUR account  

---

## 🔍 Two Possible Interpretations:

### ✅ **CURRENT (Probably Correct):**

**Scenario:** You (owner) LOANED money TO the company

```
Before:  Your personal account → Company Wise EUR
After:   Company Wise EUR has 33,609.03 SEK MORE
         Company owes you 33,609.03 SEK MORE
```

**SIE Entry:**
```
#VER A 391 20260306 "Received money from MOHAMMAD SAMI ALSHAR [WISE_EUR]"
{
   #TRANS 1944 {} 33609.03      // Bank UP (company has more money)
   #TRANS 2893 {} -33609.03     // Debt to you UP (company owes you more)
}
```

**Result:**
- ✅ Bank balance INCREASES
- ✅ Debt to you INCREASES (company must repay you later)
- This is a **LOAN** from owner to company

---

### ❌ **ALTERNATIVE (If direction is opposite):**

**Scenario:** Company PAID you back (money went OUT to owner)

```
Before:  Company Wise EUR → Your personal account
After:   Company Wise EUR has 33,609.03 SEK LESS
         Company owes you 33,609.03 SEK LESS
```

**SIE Entry would be:**
```
#VER A 391 20260306 "Sent money to MOHAMMAD SAMI ALSHAR [WISE_EUR]"
{
   #TRANS 2893 {} 33609.03      // Debt to you DOWN (you're being repaid)
   #TRANS 1944 {} -33609.03     // Bank DOWN (money leaves company)
}
```

**Result:**
- ❌ Bank balance DECREASES
- ❌ Debt to you DECREASES (company pays you back)
- This would be a **REPAYMENT** from company to owner

---

## 🎯 Which One Is Correct?

### Check your Wise EUR statement:

**Look at 06-03-2026 transaction:**
- Does it say **"Received money"** or **"Sent money"**?
- Is the balance **INCREASING** or **DECREASING**?
- Is the amount shown as **positive** (money in) or **negative** (money out)?

### From the CSV statement:

```
Type: TRANSFER
Direction: INCOMING (IN)
Description: "Received money from MOHAMMAD SAMI ALSHAREF with reference"
Amount: +2,974.25 EUR
```

**This confirms:** Money came IN → You loaned money TO the company ✅

---

## 📊 Current Balance Status:

**Opening (01-01-2026):** -1,598,927.35 SEK  
**After A391:** -1,632,536.38 SEK  
**Change:** -33,609.03 SEK  

**Negative means:** Company owes you money (liability)  
**More negative:** Company owes you MORE money  

---

## ✅ CONCLUSION

**The current entry is CORRECT.**

You transferred money FROM your personal account TO the company's Wise EUR account on 06-03-2026. This is recorded as a loan from you to the company, increasing the debt the company owes you.

---

## 🔧 If You Want to Fix It

**ONLY change it if:**
1. The Wise EUR statement shows money going OUT (not IN)
2. You actually withdrew money (not deposited)
3. The bank balance went DOWN (not UP)

**Then the entry should be reversed.**

---

**Question for you:** On 06-03-2026, did you:
- ✅ **Transfer money FROM your account TO company Wise EUR?** → Current entry is correct
- ❌ **Withdraw money FROM company Wise EUR TO your account?** → Entry needs to be reversed

Check your Wise EUR balance chart on that date to confirm!
