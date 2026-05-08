# FORENSIC AUDIT FRAMEWORK — SAMIS JACKETS AB
**Org.nr:** 559489-5301  
**Audit Date:** 2026-05-07  
**Auditor Role:** Tax Inspector / Skatteverket Investigator  
**Scope:** Full SE file and accounting ledger audit (2024-07-01 → 2026-03-31)

---

## EXECUTIVE SUMMARY - CURRENT FINANCIAL POSITION

### Balance Sheet Status (as of 2026-01-06 extract from Visma):
| Account | Description | Amount (SEK) | Status |
|---------|-------------|--------------|--------|
| **1460** | Lager handelsvaror | 982,749.46 | ⚠️ CRITICAL - Very high inventory |
| **2893** | Skulder närstående | -1,596,598.07 | ⚠️ CRITICAL - Huge related party debt |
| **2441** | Future World Tech | 194,484.72 | ⚠️ Large supplier debt |
| **5460** | Förbrukningsmaterial | -15,463.12 | ⚠️ User reports 185,000 issue |
| **Result** | Total Loss | -321,578.49 | 🔴 CRITICAL LOSS |

### RED FLAGS IDENTIFIED IMMEDIATELY:
1. **🚨 PACKAGING MATERIALS CONCERN**: User reports ~185,000 kr packaging moved to cost causing losses
2. **🚨 MASSIVE RELATED PARTY DEBT**: 1.6M kr debt to närstående (Sami) - tax scrutiny risk
3. **🚨 INVENTORY VALUATION**: ~983k kr inventory - needs verification against purchases
4. **🚨 NEGATIVE RESULT**: -321k kr loss - sustainability concern

---

## AUDIT OBJECTIVES

### PRIMARY GOALS:
1. ✅ Verify all SE file transactions comply with Swedish accounting law (BFL, ÅRL)
2. ✅ Validate account classifications per EU-BAS97
3. ✅ Identify misclassifications, errors, and tax compliance risks
4. ✅ Trace packaging materials issue (185,000 kr concern)
5. ✅ Verify inventory accounting and COGS calculations
6. ✅ Assess related party transaction (2893) documentation
7. ✅ Validate VAT (moms) calculations and reporting
8. ✅ Check for private/business separation compliance

### METHODOLOGY:
- Process ALL SE files in batches of 50 transactions
- Cross-reference against accounting methodology rules
- Flag discrepancies for review
- Document findings in structured MD files
- Mark completion status for each batch

---

## SE FILES TO AUDIT (81 files identified)

### PRIORITY 1 - Q1 2026 (Most Recent):
- [  ] MASTER_Q1_2026_CORRECTED_CASH_BASIS.se
- [  ] inventory_purchases/*.se (FWT_INVOICE, SAMER_PAYMENT)
- [  ] source_csv/sales_data/SALES_AND_COGS_STANDALONE.se
- [  ] source_csv/marginalen/*.se
- [  ] source_csv/Lunar_Bank/*.se
- [  ] source_csv/nordea/*.se
- [  ] source_csv/wise/*/*.se
- [  ] source_csv/worldline/*.se

### PRIORITY 2 - Q4 2025:
- [  ] Q4_2025_READY_FOR_VISMA_IMPORT.se
- [  ] final_se_files/INVENTORY_Q4_2025.se
- [  ] final_se_files/SALES_Q4_2025.se
- [  ] All individual bank SE files

### PRIORITY 3 - Q3 2025:
- [  ] NEW_PERIOD_2025-07_FORWARD/20250930-COMPLETE-FROM-QURAN-FINAL.se
- [  ] Individual bank and transaction files

---

## AUDIT AREAS & COMPLIANCE CHECKS

### 1. ACCOUNT CLASSIFICATION VERIFICATION
**Rules Source:** ACCOUNTING_METHODOLOGY_SAMIS_JACKETS.md

#### Bank Accounts (BAS Class 19):
- [ ] 1930 Marginalen - proper classification
- [ ] 1947 Worldline - settlement matching
- [ ] 1948 Lunar - sales account only
- [ ] 1940-1949 Wise accounts - proper currency handling
- [ ] 2893 Related party loans - proper documentation

#### Cost Accounts (BAS Class 4-6):
- [ ] 4000 Raw materials purchases
- [ ] 4110 COGS - matching to inventory sales
- [ ] 5010 Rent - proper monthly allocation
- [ ] 5460 Förbrukningsmaterial - **CRITICAL CHECK**
- [ ] 5700 Freight - proper VAT treatment
- [ ] 6570 Bank fees - completeness

#### Revenue Accounts (BAS Class 3):
- [ ] 3051 Sales 25% VAT - proper VAT calculation
- [ ] 3105 Export sales 0% VAT - documentation

### 2. VAT (MOMS) COMPLIANCE
- [ ] All 3051 sales have 25% VAT (D 1930/1948 | K 3051 + K 2611)
- [ ] Export sales (3105) have 0% VAT with proper documentation
- [ ] Input VAT (2641) properly claimed
- [ ] VAT balance (2650) reconciles to declarations

### 3. INVENTORY ACCOUNTING
- [ ] All inventory purchases to 1460
- [ ] COGS properly calculated and moved to 4110
- [ ] Period-end inventory balance verification
- [ ] FWT supplier invoices match payments

### 4. RELATED PARTY TRANSACTIONS (2893)
**TAX AUTHORITY FOCUS AREA**
- [ ] All 2893 transactions properly documented
- [ ] Interest charges appropriate (if loans >1 year)
- [ ] No hidden salary/dividends disguised as loans
- [ ] Clear business vs. private separation

### 5. PRIVATE VS BUSINESS SEPARATION
- [ ] Nordea Gold/Premium/Personkonto transactions properly classified
- [ ] Amex transactions - business only
- [ ] Remember Card - business expenses only
- [ ] Personal expenses NOT deducted

### 6. CURRENCY & FX HANDLING
- [ ] All Wise transactions converted to SEK
- [ ] FX rates documented and reasonable
- [ ] FX gains/losses to 3960/7960

---

## FINDINGS REGISTER

### Format for Each Finding:
```markdown
### FINDING #[NUMBER] - [SEVERITY]
**File:** [SE file name]
**Transaction:** [VER line]
**Issue:** [Description]
**Rule Violated:** [Reference to accounting rule]
**Impact:** [Financial/Tax/Compliance]
**Recommendation:** [Fix or justify]
**Status:** [ ] Open | [ ] Resolved | [ ] Justified
```

### Severity Levels:
- 🔴 **CRITICAL** - Major compliance violation, tax risk, material misstatement
- 🟠 **HIGH** - Significant error, correction strongly recommended
- 🟡 **MEDIUM** - Minor error, should be corrected
- 🟢 **LOW** - Inconsistency, documentation improvement

---

## BATCH PROCESSING STATUS

### Batch Structure:
Each SE file will be processed in groups of 50 transactions.
Progress tracked in separate finding files.

---

## NEXT STEPS:
1. ✅ Framework created
2. [ ] Audit Q1 2026 MASTER file - Batch 1 (transactions 1-50)
3. [ ] Continue systematic batch processing
4. [ ] Generate consolidated findings report
5. [ ] Provide remediation recommendations

---

**Audit Principle:** *"If Skatteverket was investigating this company for tax evasion, what would they find?"*

**Standard:** Swedish Accounting Act (ÅRL), Bookkeeping Act (BFL), VAT Law (ML)
