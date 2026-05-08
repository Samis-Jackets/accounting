# ✅ FINAL CORRECTED - FUTURE WORLD TECH INVOICE
## NO VAT - China Import (Outside EU)

---

## 🚨 CRITICAL CORRECTION SUMMARY

**Previous Versions (WRONG):**
- ❌ Added 25% Swedish VAT: 304,518.96 SEK
- ❌ Total payment: 1,527,594.80 SEK
- ❌ Used account 2641 (Ingående moms)
- ❌ Paid directly from 1942 (Wise USD) without using 2441

**THIS VERSION (CORRECT):**
- ✅ NO VAT (0%) - imports from China outside EU
- ✅ Invoice price ONLY: 1,218,075.84 SEK
- ✅ Uses account 2441 (Supplier debt to FWT)
- ✅ Follows historical pattern from MASTER_Q1_2026_CORRECTED_CASH_BASIS.se

---

## 📋 INVOICE DETAILS

| Item | Amount |
|------|-------:|
| **Invoice (USD)** | $126,882.90 |
| **Exchange Rate** | 9.6 SEK/USD |
| **Invoice (SEK)** | **1,218,075.84 SEK** |
| **VAT** | **0%** (China import) |
| **Total** | **1,218,075.84 SEK** |

**Supplier:** Future World Tech International Limited (Hong Kong)  
**Invoice:** FWT-SJ-2026-Q1-001  
**Invoice Date:** 2026-03-31  
**Payment Date:** 2026-03-20 (or later)

---

## 📦 PRODUCT BREAKDOWN (49,548 units)

### ACCOUNT 1460: Resellable Inventory (29,673 units)

| Product Category | Units | SEK |
|------------------|------:|----------:|
| Children's clothing | 2,965 | 28,464.00 |
| Women's outerwear | 1,107 | 51,648.19 |
| Men's mixed clothing | 1,431 | 65,940.48 |
| Women's trousers | 136 | 3,407.62 |
| Women's dresses | 223 | 14,407.58 |
| Women's mixed clothing | 350 | 15,657.60 |
| Socks | 5,100 | 4,896.00 |
| Scarves / Hijab | 2,141 | 24,869.86 |
| Handbags | 1,190 | 40,669.44 |
| Footwear | 912 | 17,247.74 |
| Rings | 3,784 | 71,926.27 |
| Earrings | 3,603 | 42,889.71 |
| Necklaces & Bracelets | 2,933 | 106,995.84 |
| Jewellery sets | 240 | 9,976.32 |
| Mixed jewellery | 1,260 | 44,996.32 |
| Dolls & toys | 162 | 10,855.30 |
| Remote control toys | 336 | 37,642.75 |
| Plastic toy shooting | 300 | 14,083.20 |
| Earphones | 1,500 | 180,000.00 |
| **SUBTOTAL** | **29,673** | **791,575.22** |

### ACCOUNT 5460: Packaging Materials (18,246 units)

| Product | Units | SEK |
|---------|------:|----------:|
| Ring boxes | 9,886 | 110,090.50 |
| Paper packaging | 8,360 | 73,835.52 |
| **SUBTOTAL** | **18,246** | **183,926.02** |

### ACCOUNT 1220: Equipment & Fixtures (1,629 units)

| Product | Units | SEK |
|---------|------:|----------:|
| Metal store fixtures | 193 | 77,817.60 |
| Display screens | 4 | 28,800.00 |
| Roller conveyor system | 10 | 27,360.00 |
| Iron display cabinet | 2 | 21,120.00 |
| Plastic mannequins | 10 | 34,272.00 |
| Jewelry display stand | 1,410 | 58,204.80 |
| **SUBTOTAL** | **1,629** | **247,574.40** |

---

## 📊 ACCOUNT SUMMARY

| Account | Category | Units | SEK | % |
|---------|----------|------:|----------:|-----:|
| **1460** | Inventory | 29,673 | 791,575.22 | 65.0% |
| **5460** | Packaging | 18,246 | 183,926.02 | 15.1% |
| **1220** | Equipment | 1,629 | 247,574.40 | 20.3% |
| **TOTAL** | | **49,548** | **1,218,075.84** | **100.0%** |

---

## 💳 SIE4 ENTRIES - TWO OPTIONS

### ⭐ OPTION 1: TWO-ENTRY METHOD (Recommended)

**Matches historical pattern from MASTER_Q1_2026_CORRECTED_CASH_BASIS.se**

**ENTRY 1: Record Invoice (Creates supplier debt)**

```
#VER A 526 20260331 "FWT Invoice FWT-SJ-2026-Q1-001 - $126,882.90 @ 9.6"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2441 {} -1218075.84
}
```

**ENTRY 2: Record Payment (Pays off supplier debt)**

```
#VER A 527 20260320 "Payment to FUTURE WORLD TECH INTERNAT [WISE_USD]"
{
   #TRANS 2441 {} 1218075.84
   #TRANS 1942 {} -1218075.84
}
```

**Balance Impact (Two-Entry Method):**
- Account 2441: Opens 610,300.17 → +1,218,075.84 (invoice) → -1,218,075.84 (payment) = 610,300.17 (unchanged)
- Account 1942: -1,218,075.84 (payment out)
- Account 1460: +791,575.22
- Account 5460: +183,926.02
- Account 1220: +242,574.60

---

### OPTION 2: SINGLE-ENTRY METHOD (Simplified cash basis)

**Use if invoice and payment happen together**

```
#VER A 526 20260320 "FWT Purchase & Payment - $126,882.90 @ 9.6 [WISE_USD]"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 1942 {} -1218075.84
}
```

**Balance Impact (Single-Entry Method):**
- Account 1942: -1,218,075.84 (payment out)
- Account 1460: +791,575.22
- Account 5460: +183,926.02
- Account 1220: +242,574.60
- Account 2441: No change (skipped since paid immediately)

---

## 💡 WHY NO VAT?

**From ACCOUNTING_METHODOLOGY_SAMIS_JACKETS.md:**

> **Regel:** Alla betalningar till `FUTURE WORLD TECH INTERNATIONAL LIMITED`  
> (via Wise USD) är **lager-anskaffning från Kina**.  
>   
> - **Konto 1460** (Lager varor) — debet  
> - **Konto 2441** (Leverantörsskuld) — kredit på fakturadag, sen  
>   debiteras 2441 / krediteras 1942 vid varje Wise-betalning.  
> - **Moms:** 0% (utanför EU, ingen ingående moms i Sverige — moms tas vid tull  
>   via tullräkning från Tullverket, bokas separat på 2645).

**Key Points:**
1. Imports from outside EU = **0% VAT** at purchase time
2. Import VAT/customs are handled **separately** through customs clearance
3. Swedish input VAT (2641) **only applies** to purchases within EU/Sweden
4. Account 2441 = Supplier debt to Future World Tech
5. Account 1942 = Wise USD bank account

---

## 📈 ACCOUNT BALANCES AFTER

| Account | Opening | Change | Closing |
|---------|--------:|-------:|--------:|
| **1460** | 566,933.00 | +791,575.22 | 1,358,508.22 |
| **1220** | 49,170.68 | +242,574.60 | 291,745.28 |
| **5460** | (varies) | +183,926.02 | (varies) |
| **2441** | 610,300.17 | 0.00 | 610,300.17 * |
| **1942** | 4,503.41 | -1,218,075.84 | -1,213,572.43 |

**\* Account 2441:** If using two-entry method, increases then decreases by same amount = net 0

---

## ✅ VALIDATION CHECKLIST

Before importing to Visma:
- [ ] Verification numbers updated (A 526, A 527)
- [ ] Dates correct (invoice date + payment date)
- [ ] Invoice number: FWT-SJ-2026-Q1-001
- [ ] Amount: $126,882.90 USD @ 9.6 = 1,218,075.84 SEK
- [ ] NO VAT (0% for China import)
- [ ] Account 2441 used (not direct to 1942)
- [ ] Entries balanced

After import:
- [ ] Account 1460 increased correctly
- [ ] Account 1220 increased correctly
- [ ] Account 5460 increased correctly
- [ ] Account 1942 decreased by payment amount
- [ ] No VAT accounts affected (2641/2611 unchanged)

---

## 📚 RELATED FILES

- **CORRECTED_INVENTORY_DATABASE.csv**: Product database with SKU/cost details
- **FWT_INVOICE_STANDALONE.se**: Standalone SIE file for direct import
- **MASTER_Q1_2026_CORRECTED_CASH_BASIS.se**: Main Q1 2026 SIE file (525 entries)

---

**Status:** ✅ FINAL CORRECTED  
**VAT:** 0% (China import outside EU)  
**Account:** 2441 (Leverantörsskulder)  
**Pattern:** Matches company's historical accounting methodology  
**Ready for:** Visma import
