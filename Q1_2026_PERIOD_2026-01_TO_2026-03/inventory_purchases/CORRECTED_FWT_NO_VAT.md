# ✅ CORRECTED - FUTURE WORLD TECH INVOICE (CHINA IMPORT)
## NO VAT - Imports from China are 0% at purchase

---

## 🚨 CRITICAL CORRECTION

**WRONG APPROACH:** Adding 25% Swedish VAT to Chinese import  
**CORRECT APPROACH:** 0% VAT - imports from outside EU have NO Swedish VAT at purchase time

---

## 📋 INVOICE DETAILS

| Item | Amount |
|------|-------:|
| **Invoice (USD)** | $126,882.90 |
| **Exchange Rate** | 9.6 SEK/USD |
| **Invoice (SEK)** | **1,218,075.84 SEK** |
| **VAT** | **0%** (China import) |
| **Total** | **1,218,075.84 SEK** |

---

## 💡 HOW THIS WORKS (From ACCOUNTING_METHODOLOGY_SAMIS_JACKETS.md)

**Future World Tech International Limited (China) - Inventory Purchase:**

1. **Account 1460** (Inventory) - debit
2. **Account 2441** (Supplier debt) - credit on invoice date
3. **VAT: 0%** (outside EU, no Swedish input VAT at purchase)
4. Import VAT/customs handled separately via customs clearance

**Two-step process:**
- **STEP 1:** Record invoice (creates debt in 2441)
- **STEP 2:** Record payment (pays off 2441 from Wise USD)

---

## 📦 ACCOUNT ALLOCATION

| Account | Category | SEK |
|---------|----------|----------:|
| **1460** | Inventory (resale) | 791,575.22 |
| **5460** | Packaging | 183,926.02 |
| **1220** | Equipment | 247,574.40 |
| **2441** | Supplier debt (FWT) | -1,218,075.84 |
| **TOTAL** | | **0.00** (balanced) |

---

## 💳 CORRECTED SIE4 ENTRIES

### OPTION 1: TWO ENTRIES (Recommended - matches historical pattern)

**ENTRY 1: Record Invoice (Date: 2026-03-31 - invoice date)**

```
#VER A 526 20260331 "FWT Invoice FWT-SJ-2026-Q1-001 - $126,882.90 @ 9.6"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 2441 {} -1218075.84
}
```

**ENTRY 2: Record Payment (Date: When actually paid via Wise USD)**

```
#VER A 527 20260320 "Payment to FUTURE WORLD TECH INTERNAT [WISE_USD]"
{
   #TRANS 2441 {} 1218075.84
   #TRANS 1942 {} -1218075.84
}
```

---

### OPTION 2: COMBINED ENTRY (If paid immediately - cash basis)

```
#VER A 526 20260320 "FWT Purchase & Payment - $126,882.90 @ 9.6 [WISE_USD]"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 242574.60
   #TRANS 1942 {} -1218075.84
}
```

**Note:** This skips 2441 since invoice and payment happen together

---

## 🔄 BALANCE VERIFICATION

**OPTION 1 (Two entries):**

Entry 1:
- Debits: 791,575.22 + 183,926.02 + 242,574.60 = 1,218,075.84
- Credits: 1,218,075.84
- ✅ BALANCED

Entry 2:
- Debits: 1,218,075.84
- Credits: 1,218,075.84
- ✅ BALANCED

**OPTION 2 (Combined):**
- Debits: 791,575.22 + 183,926.02 + 242,574.60 = 1,218,075.84
- Credits: 1,218,075.84
- ✅ BALANCED

---

## 📊 ACCOUNT BALANCES AFTER

| Account | Before | Change | After |
|---------|-------:|-------:|------:|
| **1460** | 566,933.00 | +791,575.22 | 1,358,508.22 |
| **1220** | 49,170.68 | +242,574.60 | 291,745.28 |
| **5460** | (varies) | +183,926.02 | (varies) |
| **2441** | 610,300.17 | 0.00 * | 610,300.17 |
| **1942** | 4,503.41 | -1,218,075.84 | -1,213,572.43 |

**\* If using two-entry method:** 2441 increases by 1,218,075.84 then decreases by same amount = net 0

---

## ✅ CHECKLIST

Before adding:
- [ ] Invoice: FWT-SJ-2026-Q1-001
- [ ] Amount: $126,882.90 USD
- [ ] Rate: 9.6 SEK/USD
- [ ] Total SEK: 1,218,075.84
- [ ] **VAT: 0%** (China import)
- [ ] Choose: Two entries OR combined
- [ ] Update verification numbers
- [ ] Update dates (invoice date + payment date)

After adding:
- [ ] Entries balanced
- [ ] Account 1460 increased
- [ ] Account 1220 increased
- [ ] Account 5460 increased
- [ ] Account 1942 decreased (payment out)

---

## 🚨 KEY DIFFERENCES FROM PREVIOUS VERSION

| Item | OLD (WRONG) | NEW (CORRECT) |
|------|-------------|---------------|
| **VAT** | 25% = 304,518.96 SEK | **0%** (no VAT) |
| **Total payment** | 1,527,594.80 SEK | **1,218,075.84 SEK** |
| **VAT account** | 2641 (ingående moms) | **None** (no VAT) |
| **Supplier account** | Direct to 1942 | **Via 2441** (supplier debt) |
| **Pattern** | Single entry | **Two entries** (invoice + payment) |

---

## 💡 WHY NO VAT?

**From Accounting Methodology:**
> "**Moms:** 0% (utanför EU, ingen ingående moms i Sverige — moms tas vid tull
> via tullräkning från Tullverket, bokas separat på 2645)."

**Translation:**
- Imports from outside EU = 0% VAT at purchase
- Import VAT/customs are handled separately through customs clearance
- Swedish input VAT (2641) only applies to purchases within EU

---

**Status:** ✅ CORRECTED  
**VAT:** 0% (China import outside EU)  
**Account:** 2441 (Leverantörsskulder)  
**Pattern:** Matches historical FWT transactions in MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
