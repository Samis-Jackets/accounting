# CORRECTIONS NEEDED - MOMS (VAT) EXTRACTION

## Summary
After full Lunar Bank and Marginalen audit, found 2 transactions that need MOMS extraction:

1. **IT Equipment Purchase (laptops/mobiles)** - 11,800 SEK - Currently miscoded as shareholder debt
2. **Snabbgross Food Purchase** - 3,863 SEK - Not yet recorded (cash payment from 1910)

---

## 1. IT EQUIPMENT PURCHASE - 11,800 SEK

### Current (WRONG):
```
#VER A 477 20260325 "Aterbetalning skuld delagare (sista fakturan = 2893) [MARGINALEN]"
{
   #TRANS 1930 {} -11800.00
   #TRANS 2893 {} 11800.00
}
```

**Problem:** Coded as shareholder debt repayment (2893), but this is IT equipment purchase!

### Corrected (with 25% MOMS extraction):
```
#VER A 477 20260325 "IT Equipment - Laptops and Mobiles [MARGINALEN]"
{
   #TRANS 1930 {} -11800.00
   #TRANS 5460 {} 9440.00
   #TRANS 2641 {} 2360.00
}
```

**Accounts:**
- 1930 = Marginalen Bank (cash OUT)
- 5460 = Inventarier och verktyg (IT equipment)
- 2641 = Ingående moms 25% (Input VAT to reclaim)

**Calculation:**
- Gross amount: 11,800 SEK
- Base (excluding MOMS): 11,800 / 1.25 = 9,440 SEK
- MOMS 25%: 11,800 - 9,440 = 2,360 SEK

**Note:** If invoice shows different MOMS rate or no MOMS, adjust accordingly.

---

## 2. SNABBGROSS FOOD PURCHASE - 3,863 SEK

### Currently: NOT RECORDED

### Need to ADD (with 6% MOMS extraction):
```
#VER A XXX 20260XXX "Snabbgross food/beverage purchase - Cash [KASSA]"
{
   #TRANS 1910 {} -3863.00
   #TRANS 4580 {} 3645.28
   #TRANS 2641 {} 217.72
}
```

**Accounts:**
- 1910 = Kassa (Cash)
- 4580 = Varor för återförsäljning - livsmedel (Food/beverage for resale)
- 2641 = Ingående moms 6% (Input VAT to reclaim)

**Calculation:**
- Gross amount: 3,863 SEK
- Base (excluding MOMS): 3,863 / 1.06 = 3,645.28 SEK
- MOMS 6%: 3,863 - 3,645.28 = 217.72 SEK

**Note:** Need exact date from invoice/receipt to complete verification.

---

## Impact Summary

### Before Corrections:
- Ingående moms (2641): [Current amount from SE file]
- IT Equipment expenses: 0 SEK
- Food/beverage purchases: 0 SEK
- Shareholder debt repayments: 11,800 SEK (WRONG!)

### After Corrections:
- Ingående moms (2641): **+2,577.72 SEK** (2,360 + 217.72)
- IT Equipment expenses: **9,440 SEK**
- Food/beverage purchases: **3,645.28 SEK**
- Shareholder debt repayments: **-11,800 SEK** (removed)

### VAT Impact:
**Additional 2,577.72 SEK to reclaim from Skatteverket!**

---

## Next Steps:
1. ✅ Confirm IT invoice includes 25% MOMS (check invoice)
2. ✅ Get exact date for Snabbgross purchase
3. 🔄 Update MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
4. 🔄 Recalculate all account balances
5. 🔄 Update MOMS summary
