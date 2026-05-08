# 🚀 QUICK REFERENCE - CHINA CONTAINER VAT ENTRIES
## Copy-Paste SIE4 Entries for Q1 2026

**Container:** China 2025-001  
**Total Goods:** ¥474,999.50 CNY = 665,000 SEK @ 1.40  
**Import VAT:** 188,750 SEK (25% deductible)  
**Customs Duty:** 55,000 SEK (capitalize to inventory)  

---

## 📋 STEP-BY-STEP ACCOUNTING ENTRIES

### ✅ ENTRY 1: Customs Duty + Import VAT Payment
**Date:** When customs clearance is paid (e.g., 2026-03-15)  
**Total Cash Out:** 243,750 SEK

```
#VER A 526 20260315 "Tull och importmoms - China Container 2025-001"
{
   #TRANS 1460 {} 55000.00
   #TRANS 2641 {} 188750.00
   #TRANS 1630 {} -243750.00
}
```

**What this does:**
- ➕ Adds 55,000 SEK to inventory (customs duty)
- ➕ Records 188,750 SEK deductible import VAT
- ➖ Reduces bank/tax account by 243,750 SEK

---

### ✅ ENTRY 2: Goods Purchase Payment
**Date:** When supplier is paid (e.g., 2026-03-20)  
**Total Cash Out:** 665,000 SEK

```
#VER A 527 20260320 "Lagerinköp China Container - ¥474,999.50 @ 1.40"
{
   #TRANS 1460 {} 665000.00
   #TRANS 1942 {} -665000.00
}
```

**What this does:**
- ➕ Adds 665,000 SEK to inventory (goods)
- ➖ Reduces Wise/bank account by 665,000 SEK

---

### ✅ ENTRY 3: Shipping & Logistics
**Date:** When freight/logistics is paid (e.g., 2026-03-22)  
**Total Cash Out:** 35,000 SEK

```
#VER A 528 20260322 "Frakt och logistik - China Container"
{
   #TRANS 1460 {} 35000.00
   #TRANS 1940 {} -35000.00
}
```

**What this does:**
- ➕ Adds 35,000 SEK to inventory (freight + insurance + local transport + broker)
- ➖ Reduces bank account by 35,000 SEK

---

## 💰 TOTAL CASH FLOW IMPACT

| Entry | Description | Cash Out (SEK) | Account |
|-------|-------------|----------------|---------|
| 1 | Customs + VAT | -243,750 | 1630 |
| 2 | Goods Payment | -665,000 | 1942 |
| 3 | Shipping | -35,000 | 1940 |
| **TOTAL** | | **-943,750 SEK** | |

---

## 📊 INVENTORY BALANCE IMPACT

| Component | Amount (SEK) |
|-----------|--------------|
| Opening Balance 1460 (2026-01-01) | 566,933.00 |
| + Goods (Entry 2) | 665,000.00 |
| + Customs Duty (Entry 1) | 55,000.00 |
| + Shipping (Entry 3) | 35,000.00 |
| **New Inventory Balance** | **1,321,933.00** |

**Import VAT (2641):** 188,750.00 SEK (deductible on VAT return)

---

## 🔄 WHEN GOODS ARE SOLD - EXAMPLE

### Selling Coats for 100,000 SEK (excl VAT)

**Entry A: Record Sale**
```
#VER A 600 20260420 "Försäljning kappor - China Container"
{
   #TRANS 1940 {} 125000.00
     #TRANS 3000 {} -100000.00
     #TRANS 2610 {} -25000.00
}
```

**What this does:**
- ➕ Cash received 125,000 SEK (including VAT)
- ➕ Sales revenue 100,000 SEK (excl VAT)
- ➕ Output VAT 25,000 SEK (25% charged to customer)

---

**Entry B: Cost of Goods Sold**
```
#VER A 601 20260420 "Kostnad såld vara - kappor"
{
   #TRANS 4100 {} 40000.00
     #TRANS 1460 {} -40000.00
}
```

**What this does:**
- ➕ COGS expense 40,000 SEK (cost of coats sold)
- ➖ Reduce inventory by 40,000 SEK

---

**Profit Calculation:**
```
Sales Revenue (excl VAT):     100,000 SEK
Cost of Goods Sold:           -40,000 SEK
Gross Profit:                  60,000 SEK (60% margin)

Output VAT Collected:          25,000 SEK
Import VAT Deductible:       -188,750 SEK (full amount on return)
Net VAT Effect:              Depends on total sales
```

---

## 📈 VAT RETURN (MOMSDEKLARATION) - Q1 2026

### Input VAT (Ingående moms):
```
Ruta 30: Import VAT (2641)    188,750 SEK  ✅ CLAIM THIS
```

### Output VAT (Utgående moms):
```
Ruta 10: Sales VAT (2610)     XX,XXX SEK   (sum of all sales)
```

### Net VAT:
```
If Output VAT > Input VAT:    PAY difference to Skatteverket
If Output VAT < Input VAT:    RECLAIM difference from Skatteverket
```

**Example:**
- If you sell for 800,000 SEK total in Q1:
  - Output VAT = 200,000 SEK
  - Input VAT = 188,750 SEK
  - **Net VAT to pay = 11,250 SEK**

---

## 🎯 QUICK CHECKLIST

### Before Recording Entries:
- [ ] Confirm CNY→SEK exchange rate (currently using 1.40)
- [ ] Get actual customs declaration with duty amount
- [ ] Verify import VAT amount from customs
- [ ] Have payment receipts ready
- [ ] Check next available verification number in SIE4

### Entry Details to Update:
1. **Verification Numbers:** A 526, A 527, A 528 → Use next available
2. **Dates:** 20260315, 20260320, 20260322 → Use actual payment dates
3. **Amounts:** 55000, 188750, 665000, 35000 → Use actual amounts if different
4. **Payment Accounts:** 1630, 1942, 1940 → Verify correct accounts

### After Recording:
- [ ] Update Q1 2026 SIE4 file
- [ ] Save all supporting documents
- [ ] Prepare for VAT return filing
- [ ] Track inventory movements

---

## 📝 ACCOUNT REFERENCE TABLE

| Account | Name | Type | Purpose |
|---------|------|------|---------|
| **1460** | Lager av handelsvaror | Asset | Inventory goods + duty + freight |
| **1630** | Skattekonto | Asset | Tax payments account |
| **1940** | Företagskonto/Bank | Asset | Main bank account |
| **1942** | Wise USD/CNY | Asset | Foreign currency account |
| **2641** | Ingående moms | Asset/Tax | Deductible input VAT |
| **2610** | Utgående moms | Liability | Output VAT charged to customers |
| **3000** | Försäljningsintäkter | Income | Sales revenue |
| **4100** | Varor för återförsäljning | Expense | Cost of goods sold |

---

## ⚠️ IMPORTANT REMINDERS

### Cash Basis Accounting:
✅ **Record entries ONLY when payments are made**  
❌ **Do NOT record at invoice/arrival date**  
✅ **Use actual payment dates**

### VAT Rules:
✅ **Import VAT is 100% deductible** (if goods for taxable sales)  
✅ **Must have customs declaration** as proof  
✅ **File VAT return on time** (monthly or quarterly)  
✅ **Charge 25% VAT on all Swedish sales**

### Documentation:
✅ **Keep customs declaration** (Tulldeklaration)  
✅ **Keep commercial invoice** (from Chinese supplier)  
✅ **Keep payment receipts** (bank transfers)  
✅ **Keep freight invoices** (shipping documents)

---

## 🔢 CALCULATION FORMULAS

### Import VAT:
```
Import VAT = (CIF Value + Customs Duty) × 25%
           = (700,000 + 55,000) × 0.25
           = 755,000 × 0.25
           = 188,750 SEK
```

### CIF Value:
```
CIF = FOB + Freight + Insurance + Local Transport + Broker
    = 665,000 + 25,000 + 3,500 + 4,000 + 2,500
    = 700,000 SEK
```

### Sales VAT:
```
Sales VAT = Sales Price (excl VAT) × 25%

Example: 100,000 SEK sales
Output VAT = 100,000 × 0.25 = 25,000 SEK
Total to charge customer = 125,000 SEK (incl VAT)
```

---

## 📞 NEED HELP?

### Questions About:
- **Exchange Rates:** Check xe.com or your bank rate at payment date
- **Customs Duty:** Contact Tullverket (0771-520 520) or customs broker
- **VAT Rules:** Contact Skatteverket (0771-567 567)
- **Accounting:** Consult your accountant with this document

### Related Documents:
- Full Analysis: [CHINA_CONTAINER_2025-001_VAT_ANALYSIS.md](CHINA_CONTAINER_2025-001_VAT_ANALYSIS.md)
- Q1 2026 SIE4: [../MASTER_Q1_2026_CORRECTED_CASH_BASIS.se](../MASTER_Q1_2026_CORRECTED_CASH_BASIS.se)
- Container Database: [../../China full invoices and tull and ce/shipment_database/](../../China%20full%20invoices%20and%20tull%20and%20ce/shipment_database/)

---

**Status:** ✅ READY TO USE  
**Date:** May 7, 2026  
**Cash Basis:** ✅ Confirmed - Record only when paid  
**VAT Compliant:** ✅ Per Swedish law (Mervärdesskattelagen)
