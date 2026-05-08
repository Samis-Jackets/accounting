# 🛃 CHINA CONTAINER 2025-001 - VAT & CUSTOMS DECLARATION
## Q1 2026 Import VAT Analysis - Swedish Law Compliance

**Company:** Samis Jackets AB (559489-5301)  
**Container:** China 2025-001  
**Import Period:** Q1 2026 (Estimated arrival)  
**Goods Origin:** China (Non-EU) → Sweden  
**Total Items:** 26 line items | 44,285 units  

---

## 📊 SHIPMENT SUMMARY

### Goods Value (CNY)
| Category | Items | Quantity | Total ¥ CNY |
|----------|-------|----------|-------------|
| **Clothing** | 9 | 17,719 | ¥246,668.00 |
| **Accessories** | 5 | 15,571 | ¥52,188.50 |
| **Other (ISMASH)** | 1 | 424 | ¥41,432.00 |
| **Bags** | 2 | 1,750 | ¥40,455.00 |
| **Equipment** | 4 | 207 | ¥26,540.00 |
| **Toys** | 1 | N/A | ¥23,456.00 |
| **Packaging** | 2 | 7,272 | ¥21,780.00 |
| **Shoes** | 1 | 1,340 | ¥20,300.00 |
| **Display** | 1 | 2 | ¥2,180.00 |
| **TOTAL** | **26** | **44,285** | **¥474,999.50** |

### Resellable vs. Non-Resellable
| Type | Categories | Total ¥ CNY | % of Total |
|------|------------|-------------|------------|
| **✅ Resellable** | Clothing, Accessories, Bags, Shoes, Toys, Some Packaging, Other | ¥441,279.50 | 92.9% |
| **❌ Store Use** | Equipment, Display, Some Packaging | ¥33,720.00 | 7.1% |
| **TOTAL** | | **¥474,999.50** | **100%** |

---

## 💱 CURRENCY CONVERSION (CNY → SEK)

### Exchange Rate Options:
1. **Conservative Rate:** 1.30 SEK/CNY
2. **Mid-Range Rate:** 1.40 SEK/CNY (RECOMMENDED)
3. **High Rate:** 1.50 SEK/CNY

### Goods Value in SEK (@ 1.40 rate):

```
¥474,999.50 CNY × 1.40 SEK/CNY = 664,999.30 SEK
```

**ROUNDED FOR ACCOUNTING:** **665,000 SEK**

---

## 🚢 CIF VALUE CALCULATION (Cost, Insurance, Freight)

### Components:
| Item | Amount (SEK) | Notes |
|------|--------------|-------|
| **FOB Value (Goods)** | 665,000.00 | Factory price converted |
| **Sea Freight** | 25,000.00 | Estimated Hong Kong → Gothenburg |
| **Insurance** | 3,500.00 | ~0.5% of goods value |
| **Local Transport** | 4,000.00 | Gothenburg → Eskilstuna |
| **Customs Broker Fee** | 2,500.00 | Clearance and handling |
| **CIF TOTAL** | **700,000.00 SEK** | Taxable base for duty |

---

## 🛃 CUSTOMS DUTY CALCULATION

### Harmonized System (HS) Codes & Duty Rates:
| Category | HS Code Range | Typical Duty Rate | Goods Value (SEK) | Est. Duty (SEK) |
|----------|---------------|-------------------|-------------------|-----------------|
| Clothing | 6101-6117 | 12% | 345,335 | 41,440 |
| Accessories | 7117, 4203 | 4-6% | 73,064 | 3,653 |
| Bags | 4202 | 3-5% | 56,637 | 2,265 |
| Shoes | 6401-6405 | 8% | 28,420 | 2,274 |
| Toys | 9503 | 0% | 32,838 | 0 |
| Packaging | 4819, 4821 | 0-3% | 30,492 | 305 |
| ISMASH (Other) | TBD | 6-8% | 58,005 | 4,060 |
| Equipment | 9403, 8471 | 0-2.5% | 37,156 | 464 |
| Display | 9403 | 0-2.5% | 3,053 | 31 |

**TOTAL ESTIMATED CUSTOMS DUTY:** **54,492 SEK** (rounded: **55,000 SEK**)

---

## 🇸🇪 SWEDISH IMPORT VAT (MOMS) CALCULATION

### Formula per Swedish Law:
```
Import VAT = 25% × (CIF Value + Customs Duty)
```

### Calculation:
```
Taxable Base = CIF Value + Customs Duty
Taxable Base = 700,000 SEK + 55,000 SEK = 755,000 SEK

Import VAT (25%) = 755,000 × 0.25 = 188,750 SEK
```

**IMPORT VAT TO PAY:** **188,750 SEK**

---

## 📝 SIE4 ACCOUNTING ENTRIES - Q1 2026

### ENTRY 1: Import Customs Duty & VAT Payment
**When customs clearance is paid:**

```
#VER A XXX 20260315 "Tull och importmoms - China Container 2025-001"
{
   #TRANS 1460 {} 55000.00          // Customs duty → capitalize to inventory
   #TRANS 2641 {} 188750.00         // Import VAT → DEDUCTIBLE input VAT
   #TRANS 1630 {} -243750.00        // Payment from tax account/bank
}
```

**Explanation:**
- **1460** - Lager av handelsvaror: Customs duty INCREASES inventory cost
- **2641** - Ingående moms: Import VAT is DEDUCTIBLE (claim on VAT return)
- **1630** - Skattekonto: Tax account or bank used for payment

---

### ENTRY 2: Inventory Purchase (Goods Payment)
**When payment is made to Chinese supplier:**

```
#VER A YYY 20260320 "Lagerinköp China Container 2025-001 - ¥474,999.50 @ 1.40"
{
   #TRANS 1460 {} 665000.00         // Inventory goods
   #TRANS 1942 {} -665000.00        // Payment account (Wise or bank)
}
```

**Explanation:**
- **1460** - Lager av handelsvaror: Goods at FOB value
- **1942** - Wise USD/CNY account (or relevant payment account)

---

### ENTRY 3: Shipping & Handling Costs
**When freight and logistics are paid:**

```
#VER A ZZZ 20260322 "Frakt och logistik - China Container"
{
   #TRANS 1460 {} 35000.00          // Add to inventory cost (freight + insurance + local)
   #TRANS 1940 {} -35000.00         // Payment from bank account
}
```

**Explanation:**
- Freight (25,000), insurance (3,500), local transport (4,000), broker fee (2,500) = 35,000 SEK
- All these costs are CAPITALIZED to inventory (part of acquisition cost)

---

### COMBINED INVENTORY EFFECT:

| Component | Amount (SEK) | Account |
|-----------|--------------|---------|
| Goods (FOB) | 665,000 | 1460 |
| Shipping & Logistics | 35,000 | 1460 |
| Customs Duty | 55,000 | 1460 |
| **TOTAL INVENTORY VALUE** | **755,000 SEK** | **1460** |
| | | |
| Import VAT (DEDUCTIBLE) | 188,750 | 2641 |

---

## 📤 OUTGOING VAT (SALES) - WHEN GOODS ARE SOLD

### When Selling to Swedish Customers:

**Example: Selling 100 coats for 500 SEK each (50,000 SEK + VAT)**

```
#VER A AAA 20260415 "Försäljning kappor - 100 st"
{
   #TRANS 1940 {} 62500.00          // Customer payment (including VAT)
     #TRANS 3000 {} -50000.00       // Sales revenue (excl VAT)
     #TRANS 2610 {} -12500.00       // Output VAT 25% (50,000 × 0.25)
}
```

**At the same time, record Cost of Goods Sold (COGS):**

```
#VER A AAB 20260415 "Kostnad såld vara - 100 kappor"
{
   #TRANS 4100 {} 12500.00          // COGS (cost per coat × 100)
     #TRANS 1460 {} -12500.00       // Reduce inventory
}
```

**Explanation:**
- **3000** - Försäljningsintäkter: Sales revenue (excl VAT)
- **2610** - Utgående moms: Output VAT 25% (CHARGED to customer)
- **4100** - Varor för återförsäljning: Cost of goods sold
- **1460** - Lager: Reduce inventory by cost value

---

## 🔄 VAT FLOW SUMMARY (IN vs. OUT)

### IMPORT VAT (IN) - DEDUCTIBLE:
```
Import VAT Paid (2641):        188,750 SEK  ← DEDUCTIBLE
```

### SALES VAT (OUT) - PAYABLE:
```
Sales VAT Collected (2610):    Variable     ← DEPENDS ON SALES
```

### NET VAT TO PAY/RECLAIM:
```
Net VAT = Output VAT (2610) - Input VAT (2641)

Example:
If you sell goods for 1,000,000 SEK:
- Output VAT collected: 250,000 SEK (25% of 1,000,000)
- Input VAT deductible: 188,750 SEK
- NET VAT to pay Skatteverket: 61,250 SEK

If you sell goods for 755,200 SEK (same as taxable base):
- Output VAT collected: 188,800 SEK
- Input VAT deductible: 188,750 SEK
- NET VAT to pay: 50 SEK (almost break-even)
```

**VAT NEUTRALITY:** Import VAT is refunded through sales VAT deduction.

---

## ⚖️ SWEDISH VAT LAW COMPLIANCE

### Legal Requirements (Mervärdesskattelagen):

1. **Import VAT Declaration:**
   - Must be declared when goods clear customs
   - Recorded in VAT return (momsdeklaration) for the period
   - Deductible in the same or next VAT period

2. **Input VAT (2641):**
   - Import VAT is 100% deductible if goods are for taxable sales
   - Must have customs declaration (Tulldeklaration) as documentation
   - Claim on VAT return (Ruta 30 - Ingående moms)

3. **Output VAT (2610):**
   - 25% standard rate applies to most goods (clothing, accessories, bags, shoes)
   - Must charge VAT on all Swedish sales
   - Report on VAT return (Ruta 10 - Utgående moms)

4. **Exempt Items:**
   - Children's clothing and shoes MAY be exempt or reduced rate (check specific rules)
   - Equipment for own use: Input VAT still deductible if business-related

---

## 📋 REQUIRED DOCUMENTATION

### For Import VAT Deduction:
- [x] **Customs Declaration (Tulldeklaration)** - Proof of import VAT paid
- [x] **Commercial Invoice** - From Chinese supplier (¥474,999.50)
- [x] **Bill of Lading (B/L)** - Proof of shipment
- [x] **Insurance Certificate** - Part of CIF value
- [x] **Payment Receipts** - Bank transfers for goods + customs
- [x] **Freight Invoice** - Shipping costs documentation

### For Sales VAT:
- [x] **Sales Invoices** - Must show VAT separately (25%)
- [x] **VAT Return (Momsdeklaration)** - Monthly or quarterly filing
- [x] **Sales Register** - Detailed record of all sales with VAT

---

## 💰 CASH FLOW IMPACT

### Initial Outlay (Q1 2026):
| Item | Amount (SEK) | When |
|------|--------------|------|
| Goods Payment | 665,000 | At purchase |
| Shipping & Logistics | 35,000 | At shipping |
| Customs Duty | 55,000 | At customs clearance |
| Import VAT | 188,750 | At customs clearance |
| **TOTAL CASH OUT** | **943,750 SEK** | Q1 2026 |

### VAT Recovery:
| Item | Amount (SEK) | When |
|------|--------------|------|
| Import VAT Deduction | 188,750 | VAT return Q1 or Q2 2026 |
| Sales VAT Collection | Variable | As goods are sold |

**NET INVENTORY COST:** 755,000 SEK (after VAT recovery)

---

## 📊 INVENTORY BREAKDOWN BY CATEGORY

### Resellable Goods (92.9% of shipment):

| Category | Cost (SEK) | Est. Retail (SEK) | Est. Output VAT (SEK) |
|----------|------------|-------------------|----------------------|
| Clothing | 345,335 | 900,000 | 225,000 |
| Accessories | 73,064 | 180,000 | 45,000 |
| ISMASH | 58,005 | 145,000 | 36,250 |
| Bags | 56,637 | 140,000 | 35,000 |
| Shoes | 28,420 | 75,000 | 18,750 |
| Toys | 32,838 | 80,000 | 20,000 |
| **SUBTOTAL** | **594,299** | **1,520,000** | **380,000** |

**Estimated Profit:** 1,520,000 - 594,299 = 925,701 SEK (156% markup)  
**Net VAT to Pay:** 380,000 - 188,750 = 191,250 SEK

---

## ⚠️ SPECIAL CONSIDERATIONS

### 1. Equipment & Display Items (Non-Resellable):
- **Cost:** 37,156 + 3,053 = 40,209 SEK
- **Purpose:** Store fixtures, not for resale
- **VAT Treatment:** Input VAT STILL deductible (business equipment)
- **Accounting:** May capitalize to fixed assets (account 1200-1299) instead of 1460

### 2. Packaging Items:
- **Cost:** 30,492 SEK
- **Some resellable** (gift wrapping), some for internal use (boxes)
- **VAT Treatment:** Deductible regardless of use

### 3. Toys:
- **Special Note:** CE certificates required for EU/Sweden
- **VAT:** Standard 25% rate applies
- **Safety:** Must comply with Swedish toy safety regulations

---

## 🎯 ACTION CHECKLIST

### Import Stage (Q1 2026):
- [ ] Verify CNY→SEK exchange rate at payment date
- [ ] Obtain customs declaration with exact duty amount
- [ ] Pay customs duty + import VAT (estimated 243,750 SEK)
- [ ] Record Entry 1 (customs + VAT) with actual amounts
- [ ] Record Entry 2 (goods purchase) with actual exchange rate
- [ ] Record Entry 3 (shipping costs) with actual amounts
- [ ] Save all documentation (customs, invoices, B/L, receipts)
- [ ] Claim import VAT on Q1 or Q2 VAT return

### Sales Stage (Q1-Q4 2026):
- [ ] Set retail prices with 25% VAT included
- [ ] Issue proper sales invoices showing VAT separately
- [ ] Record each sale with Output VAT (2610)
- [ ] Record COGS and reduce inventory (1460)
- [ ] File VAT returns on time (monthly or quarterly)
- [ ] Pay net VAT to Skatteverket

### Reporting:
- [ ] Update MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
- [ ] Track inventory movements in account 1460
- [ ] Monitor VAT account balances (2641 vs 2610)
- [ ] Reconcile with bank statements

---

## 📞 CONTACTS & RESOURCES

### Skatteverket (Swedish Tax Agency):
- **Phone:** 0771-567 567
- **Website:** skatteverket.se
- **VAT Info:** skatteverket.se/moms

### Customs (Tullverket):
- **Phone:** 0771-520 520
- **Website:** tullverket.se
- **HS Code Lookup:** tullverket.se/tulltaxan

### Your Accountant:
- Confirm exchange rate methodology
- Verify HS code classifications
- Review VAT return filing

---

## 📝 SUMMARY TABLE

| **Item** | **Amount (SEK)** | **Account** | **VAT Treatment** |
|----------|------------------|-------------|-------------------|
| Goods (FOB) | 665,000 | 1460 | Basis for import VAT |
| Shipping & Logistics | 35,000 | 1460 | Part of CIF |
| **CIF Total** | **700,000** | | |
| Customs Duty | 55,000 | 1460 | Capitalized to inventory |
| **Taxable Base** | **755,000** | | |
| Import VAT (25%) | 188,750 | 2641 | ✅ DEDUCTIBLE |
| **Total Inventory** | **755,000** | **1460** | |
| **Total Cash Out** | **943,750** | | Incl. VAT |
| **VAT Recovery** | **-188,750** | **2641** | Claim on return |
| **Net Cost** | **755,000** | | After VAT |

---

**Document Created:** May 7, 2026  
**Status:** ✅ COMPLETE - VAT calculations per Swedish law  
**Action Required:** Verify actual customs declaration amounts when available  
**Cash Basis Note:** Record ALL entries only when payments are actually made

---

## 🔗 RELATED FILES

- Source Data: `China full invoices and tull and ce/shipment_database/`
- Q1 2026 SIE4: `Q1_2026_PERIOD_2026-01_TO_2026-03/MASTER_Q1_2026_CORRECTED_CASH_BASIS.se`
- Accounting Rules: `master-branch/ACCOUNTING_METHODOLOGY_SAMIS_JACKETS.md`
