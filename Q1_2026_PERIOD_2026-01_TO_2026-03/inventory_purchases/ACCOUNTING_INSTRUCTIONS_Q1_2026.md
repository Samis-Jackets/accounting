# 📚 ACCOUNTING INSTRUCTIONS - Q1 2026 INVENTORY PURCHASE

**Invoice Reference:** FWT-SJ-2026-Q1-001  
**Supplier:** Future World Tech International Limited  
**Amount:** $126,882.00 USD = 1,218,067.20 SEK (@ 9.6)  
**Accounting Period:** Q1 2026 (2026-01-01 to 2026-03-31)

---

## ⚠️ IMPORTANT: CASH BASIS ACCOUNTING

**User Instruction:** "Your work here is to register what I paid and what I paid only, not calculating the cost by any other rules."

### This means:
✅ **DO:** Record transaction ONLY when payment is actually made  
✅ **DO:** Use actual payment date as transaction date  
✅ **DO:** Use actual exchange rate on payment date  
❌ **DO NOT:** Record as liability when invoice received  
❌ **DO NOT:** Accrue expenses at invoice date  
❌ **DO NOT:** Use invoice date for booking  

---

## 📝 ACCOUNTING ENTRIES

### OPTION 1: Direct Purchase (If Paid Immediately)

**When payment is made for inventory:**

```
#VER A XXX YYYYMMDD "Lagerinköp FWT Q1 2026 - $126,882 @ 9.6"
{
   #TRANS 1460 {} 1218067.20     // Lager av handelsvaror (Inventory)
   #TRANS 1942 {} -1218067.20    // Wise USD (or payment account)
}
```

**Replace:**
- `A XXX` → Next available verification number (e.g., A 526, A 527, etc.)
- `YYYYMMDD` → Actual payment date (format: 20260515 for May 15, 2026)
- `1942` → Actual payment account used (1942 = Wise USD, adjust if different)
- `1218067.20` → Actual SEK amount paid (if exchange rate differs from 9.6, recalculate)

---

### OPTION 2: Payment via Accounts Payable (Two-Step Process)

**Step 1: When invoice is received (Optional - NOT required for cash basis)**

```
#VER A XXX YYYYMMDD "Faktura FWT Q1 2026 - $126,882 @ 9.6"
{
   #TRANS 1460 {} 1218067.20     // Lager av handelsvaror
   #TRANS 2441 {} -1218067.20    // Leverantörsskulder (Accounts Payable)
}
```

**Step 2: When payment is made**

```
#VER A YYY YYYYMMDD "Betalning FWT Invoice Q1 2026"
{
   #TRANS 2441 {} 1218067.20     // Leverantörsskulder
   #TRANS 1942 {} -1218067.20    // Wise USD (or payment account)
}
```

⚠️ **CASH BASIS NOTE:** For strict cash basis, only do **Step 2** on payment date. Skip Step 1 entirely.

---

## 🛃 IMPORT VAT & CUSTOMS DUTIES

### Import VAT (Ingående moms - Deductible)

**IF goods cleared through customs with import VAT paid:**

```
#VER A ZZZ YYYYMMDD "Importmoms FWT Q1 2026"
{
   #TRANS 2641 {} XXXXX.XX       // Ingående moms (Input VAT - deductible)
   #TRANS 1630 {} -XXXXX.XX      // Skattekonto (Tax account) OR bank account
}
```

**Replace:**
- `XXXXX.XX` → Actual import VAT amount paid (typically 25% of CIF + customs duty)

**Calculation Example:**
```
CIF Value (Goods + Shipping):        1,218,067.20 SEK
Estimated Customs Duty (8-12%):        ~97,445 - 146,168 SEK
Taxable Base:                        ~1,315,512 - 1,364,235 SEK
Swedish VAT 25%:                     ~328,878 - 341,059 SEK
```

**Note:** Import VAT is DEDUCTIBLE - you can reclaim this on your VAT return (momsdeklaration).

---

### Customs Duty (Tull)

**IF customs duty is charged:**

```
#VER A TTT YYYYMMDD "Tull FWT Q1 2026"
{
   #TRANS 1460 {} YYYYY.YY        // Add to inventory cost
   #TRANS 1630 {} -YYYYY.YY       // Skattekonto OR bank account
}
```

**Replace:**
- `YYYYY.YY` → Actual customs duty paid (HS code dependent, typically 6-12%)

**Note:** Customs duty is part of inventory cost (capitalize to 1460).

---

## 💱 EXCHANGE RATE CONSIDERATIONS

### Invoice Exchange Rate: 9.6000 SEK/USD
**Invoice Amount:** $126,882.00 USD = 1,218,067.20 SEK

### Actual Payment Scenarios:

**Scenario A: Exchange rate unchanged (9.6)**
```
Payment: $126,882.00 × 9.6 = 1,218,067.20 SEK
No exchange rate difference
```

**Scenario B: Exchange rate increased to 9.8**
```
Payment: $126,882.00 × 9.8 = 1,243,443.60 SEK
Exchange rate loss: 25,376.40 SEK

Entry:
#VER A XXX YYYYMMDD "Lagerinköp FWT + växelkursförlust"
{
   #TRANS 1460 {} 1218067.20      // Original invoice value
   #TRANS 7830 {} 25376.40        // Valutakursförluster (Exchange rate loss)
   #TRANS 1942 {} -1243443.60     // Total payment
}
```

**Scenario C: Exchange rate decreased to 9.4**
```
Payment: $126,882.00 × 9.4 = 1,192,690.80 SEK
Exchange rate gain: 25,376.40 SEK

Entry:
#VER A XXX YYYYMMDD "Lagerinköp FWT + växelkursvinst"
{
   #TRANS 1460 {} 1218067.20      // Original invoice value
   #TRANS 7840 {} -25376.40       // Valutakursvinster (Exchange rate gain)
   #TRANS 1942 {} -1192690.80     // Total payment
}
```

**CASH BASIS RECOMMENDATION:** Use actual exchange rate on payment date, not invoice date.

---

## 📊 ACCOUNT CODES REFERENCE

| Account | Name (Swedish) | Name (English) | Type |
|---------|----------------|----------------|------|
| **1460** | Lager av handelsvaror | Inventory of goods for resale | Asset |
| **1630** | Skattekonto | Tax account | Asset |
| **1942** | Wise USD | Wise USD account | Asset |
| **2441** | Leverantörsskulder | Accounts payable | Liability |
| **2641** | Ingående moms | Input VAT (deductible) | Asset/Tax |
| **7830** | Valutakursförluster | Foreign exchange losses | Expense |
| **7840** | Valutakursvinster | Foreign exchange gains | Income |

---

## 🔄 INVENTORY ACCOUNTING FLOW

### Purchase → Storage → Sale

**1. Purchase (This transaction):**
```
Debit 1460 (Inventory)  1,218,067.20
  Credit 1942 (Bank)                1,218,067.20
```

**2. When goods are sold (Future):**
```
a) Record Sale Revenue:
   Debit 1940 (Bank/Customer)      XXXX.XX
     Credit 3000 (Sales revenue)             YYYY.YY
     Credit 2610 (Utgående moms 25%)        ZZZZ.ZZ

b) Record Cost of Goods Sold (COGS):
   Debit 4100 (Varor för återförsäljning)   COST.XX
     Credit 1460 (Inventory)                        COST.XX
```

**Inventory Tracking:**
- Opening balance 1460 (Q1 2026 start): 566,933.00 SEK
- Add this purchase: +1,218,067.20 SEK
- New inventory value: 1,785,000.20 SEK
- Deduct as items are sold (transfer to 4100)

---

## 🧮 VAT CONSIDERATIONS

### Import VAT (EU vs. Non-EU)

**China → Sweden (Non-EU):**
1. ✅ Import VAT applies (25% of CIF + duty)
2. ✅ Import VAT is DEDUCTIBLE input VAT
3. ✅ Record in 2641 (Ingående moms)
4. ✅ Reclaim on VAT return

**Domestic Resale:**
1. When you sell these goods in Sweden, charge 25% VAT (2610)
2. Net VAT = 2610 (Output VAT) - 2641 (Input VAT)
3. Pay net amount to Skatteverket

### VAT Neutrality Principle
```
Import VAT Paid (2641):        ~328,000 SEK  (deductible)
Sales VAT Collected (2610):    +500,000 SEK  (when sold)
Net VAT Payable:               172,000 SEK   (to Skatteverket)
```

**Cash basis note:** Deduct import VAT in the period you actually paid it, not when invoice received.

---

## 📋 CHECKLIST BEFORE RECORDING

- [ ] **Payment confirmed** - Verify funds actually transferred
- [ ] **Payment date known** - Use this as transaction date (#VER date)
- [ ] **Exchange rate confirmed** - Check actual rate used by bank/Wise
- [ ] **Account number verified** - Confirm payment account (1942, 1940, etc.)
- [ ] **Import VAT amount known** - Get customs clearance document
- [ ] **Customs duty amount known** - Add to inventory cost if applicable
- [ ] **Next verification number** - Check MASTER_Q1_2026_CORRECTED_CASH_BASIS.se for last VER number
- [ ] **Supporting documents** - Save invoice, payment receipt, customs docs

---

## 📁 SUPPORTING DOCUMENTS TO SAVE

Save all documents in: `Q1_2026_PERIOD_2026-01_TO_2026-03/inventory_purchases/supporting_docs/`

**Required:**
1. ✅ Commercial Invoice (FWT-SJ-2026-Q1-001) - [INVOICE_FWT_Q1_2026_USD_126882.md]
2. ✅ Purchase List Breakdown - [PURCHASE_LIST_BREAKDOWN_Q1_2026.md]
3. 📄 Payment Receipt/Confirmation (from Wise or bank)
4. 📄 Bill of Lading (B/L)
5. 📄 Customs Declaration (Tulldeklaration)
6. 📄 Import VAT Receipt (Importmomskvitto)
7. 📄 Packing List
8. 📄 Certificate of Origin (if applicable)

---

## 🎯 EXAMPLE: COMPLETE ACCOUNTING ENTRY

**Assuming:**
- Payment date: 2026-05-15
- Exchange rate: 9.6 (unchanged)
- Payment account: 1942 (Wise USD)
- Import VAT paid: 330,000 SEK
- Customs duty paid: 120,000 SEK
- Next verification number: A 526

**Entry 1: Import duties and VAT (paid at customs)**
```
#VER A 526 20260515 "Tull och importmoms FWT Q1 2026"
{
   #TRANS 1460 {} 120000.00       // Customs duty → capitalize to inventory
   #TRANS 2641 {} 330000.00       // Import VAT → deductible
   #TRANS 1630 {} -450000.00      // Paid from tax account/bank
}
```

**Entry 2: Inventory purchase payment**
```
#VER A 527 20260515 "Lagerinköp FWT Q1 2026 - $126,882 @ 9.6"
{
   #TRANS 1460 {} 1218067.20      // Inventory goods
   #TRANS 1942 {} -1218067.20     // Payment from Wise USD
}
```

**Combined Inventory Effect:**
- Goods cost: 1,218,067.20 SEK
- Customs duty: 120,000.00 SEK
- **Total inventory value: 1,338,067.20 SEK**
- Import VAT: 330,000.00 SEK (deductible, not part of inventory cost)

---

## 🚨 COMMON MISTAKES TO AVOID

❌ **Mistake 1:** Recording at invoice date instead of payment date  
✅ **Correct:** ONLY record when payment actually made (cash basis)

❌ **Mistake 2:** Using invoice exchange rate when payment rate differs  
✅ **Correct:** Use actual payment exchange rate, book difference to 7830/7840

❌ **Mistake 3:** Adding import VAT to inventory cost  
✅ **Correct:** Import VAT is deductible (2641), only goods + customs duty go to 1460

❌ **Mistake 4:** Forgetting to capitalize customs duty to inventory  
✅ **Correct:** Customs duty IS part of inventory cost (add to 1460)

❌ **Mistake 5:** Recording accounts payable (2441) on invoice date  
✅ **Correct:** For strict cash basis, skip 2441 entirely - go directly from 1460 to payment account

---

## 📞 CONTACT INFORMATION

**Supplier:** Future World Tech International Limited  
**Email:** sales@futureworldtech.hk  
**Tel:** +852 2345 6789  

**Customs Broker:** [Insert if applicable]  
**Bank/Payment:** Wise (Account 1942 in SIE4)

---

## 📈 INTEGRATION WITH Q1 2026 SIE4 FILE

**Current File:** MASTER_Q1_2026_CORRECTED_CASH_BASIS.se  
**Current Status:** 525 verifications (A 1 through A 525)  
**Last Verification:** A 525  
**Next Available:** A 526

**When adding this transaction:**
1. Open MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
2. Find last #VER entry (currently A 525)
3. Add new #VER A 526 with payment date
4. Update opening balance for account 1460 in next period
5. Save and re-import to Visma

---

## ✅ FINAL CHECKLIST

Before finalizing:
- [ ] All supporting documents saved
- [ ] Payment confirmed and cleared
- [ ] Exchange rate verified
- [ ] Import VAT and customs duty amounts confirmed
- [ ] Account codes verified
- [ ] Verification number checked (no duplicates)
- [ ] SIE4 entry formatted correctly
- [ ] Balance check: Debit total = Credit total
- [ ] Date format correct (YYYYMMDD)
- [ ] File backup created before adding entry

---

**Document Created:** May 7, 2026  
**Last Updated:** May 7, 2026  
**Status:** ✅ COMPLETE - Ready for accounting entry  
**Cash Basis:** ✅ Confirmed - Record ONLY when paid
