# 📦 SIMPLE INVOICE PROCESSING - $126,882.90 USD
## Samis Jackets AB | Q1 2026 | Future World Tech

---

## 💰 INVOICE TOTAL (NO ADDITIONAL COSTS)

| Item | Amount |
|------|-------:|
| **Invoice Total (USD)** | $126,882.90 |
| **Exchange Rate** | 9.6 SEK/USD |
| **Invoice Total (SEK)** | **1,218,075.84 SEK** |
| **VAT 25% on Invoice** | **304,518.96 SEK** |
| **Total with VAT** | **1,522,594.80 SEK** |

**NO freight, NO customs, NO additional costs. Invoice price is the ONLY cost.**

---

## 📦 PRODUCT BREAKDOWN BY ACCOUNT

### ACCOUNT 1460: RESELLABLE INVENTORY (29,673 units)

| Product | Qty | Unit USD | Total USD | Total SEK | HS Code |
|---------|----:|----------:|-----------:|----------:|---------|
| Children's clothing | 2,965 | 1.00 | 2,965.00 | 28,464.00 | 62099000 |
| Women's outerwear | 1,107 | 4.86 | 5,380.02 | 51,648.19 | 62049900 |
| Men's mixed clothing | 1,431 | 4.80 | 6,868.80 | 65,940.48 | 62034900 |
| Women's trousers | 136 | 2.61 | 354.96 | 3,407.62 | 62049900 |
| Women's dresses | 223 | 6.73 | 1,500.79 | 14,407.58 | 62049900 |
| Women's mixed clothing | 350 | 4.66 | 1,631.00 | 15,657.60 | 62049900 |
| Socks | 5,100 | 0.10 | 510.00 | 4,896.00 | 61159500 |
| Scarves / Hijab | 2,141 | 1.21 | 2,590.61 | 24,869.86 | 62149000 |
| Handbags | 1,190 | 3.56 | 4,236.40 | 40,669.44 | 42022900 |
| Footwear | 912 | 1.97 | 1,796.64 | 17,247.74 | 64029900 |
| Rings | 3,784 | 1.98 | 7,492.32 | 71,926.27 | 71171900 |
| Earrings | 3,603 | 1.24 | 4,467.72 | 42,889.71 | 71171900 |
| Necklaces & Bracelets | 2,933 | 3.80 | 11,145.40 | 106,995.84 | 71171900 |
| Jewellery sets | 240 | 4.33 | 1,039.20 | 9,976.32 | 71171900 |
| Mixed jewellery | 1,260 | 3.72 | 4,687.20 | 44,996.32 | 71171900 |
| Dolls & toys | 162 | 6.98 | 1,130.76 | 10,855.30 | 95030095 |
| Remote control toys | 336 | 11.67 | 3,921.12 | 37,642.75 | 95030075 |
| Plastic toy shooting | 300 | 4.89 | 1,467.00 | 14,083.20 | 95030081 |
| Earphones | 1,500 | 12.50 | 18,750.00 | 180,000.00 | 85183000 |
| **SUBTOTAL 1460** | **29,673** | | **82,434.94** | **791,575.22** | |

---

### ACCOUNT 5460: PACKAGING MATERIALS (18,246 units)

| Product | Qty | Unit USD | Total USD | Total SEK | HS Code |
|---------|----:|----------:|-----------:|----------:|---------|
| Ring boxes | 9,886 | 1.16 | 11,467.76 | 110,090.50 | 48192000 |
| Paper packaging | 8,360 | 0.92 | 7,691.20 | 73,835.52 | 48119000 |
| **SUBTOTAL 5460** | **18,246** | | **19,158.96** | **183,926.02** | |

---

### ACCOUNT 1220: EQUIPMENT (1,629 units)

| Product | Qty | Unit USD | Total USD | Total SEK | HS Code |
|---------|----:|----------:|-----------:|----------:|---------|
| Metal store fixtures | 193 | 42.00 | 8,106.00 | 77,817.60 | 94032080 |
| Display screens | 4 | 750.00 | 3,000.00 | 28,800.00 | 85285900 |
| Roller conveyor system | 10 | 285.00 | 2,850.00 | 27,360.00 | 95069990 |
| Iron display cabinet | 2 | 1,100.00 | 2,200.00 | 21,120.00 | 94036010 |
| Plastic mannequins | 10 | 357.00 | 3,570.00 | 34,272.00 | 96180000 |
| Jewelry display stand | 1,410 | 4.30 | 6,063.00 | 58,204.80 | 94032080 |
| **SUBTOTAL 1220** | **1,629** | | **25,789.00** | **247,574.40** | |

---

## 📊 ACCOUNT SUMMARY

| Account | Category | Units | SEK | % |
|---------|----------|------:|----------:|-----:|
| **1460** | Inventory (resale) | 29,673 | 791,575.22 | 65.00% |
| **5460** | Packaging | 18,246 | 183,926.02 | 15.10% |
| **1220** | Equipment | 1,629 | 247,574.40 | 20.32% |
| **TOTAL** | | **49,548** | **1,218,075.84** | **100.00%** |

---

## 💳 SIE4 ENTRIES (CASH BASIS)

### METHOD 1: PURCHASE WITH INPUT VAT (When paying supplier)

**Date: 2026-03-20 (UPDATE WITH ACTUAL PAYMENT DATE)**

```
#VER A 526 20260320 "Varuinköp FWT - Invoice $126,882.90 @ 9.6 [WISE USD]"
{
   #TRANS 1460 {} 791575.22      // Resellable inventory
   #TRANS 5460 {} 183926.02      // Packaging materials
   #TRANS 1220 {} 247574.40      // Equipment & fixtures
   #TRANS 2641 {} 304518.96      // Input VAT 25% (deductible)
   #TRANS 1942 {} -1527594.80    // Payment Wise USD (with VAT)
}
```

**Balance check:** 
- Debits: 791,575.22 + 183,926.02 + 247,574.40 + 304,518.96 = 1,527,594.60
- Credits: 1,527,594.80
- **ERROR: 0.20 SEK rounding - ADJUST**

---

### CORRECTED ENTRY:

```
#VER A 526 20260320 "Varuinköp FWT - Invoice $126,882.90 @ 9.6 [WISE USD]"
{
   #TRANS 1460 {} 791575.22
   #TRANS 5460 {} 183926.02
   #TRANS 1220 {} 247574.40
   #TRANS 2641 {} 304518.96
   #TRANS 1942 {} -1527594.60
}
```

---

## 🔄 VAT TREATMENT (BOTH SIDES)

### INPUT VAT (Ingående moms - 2641):
When you BUY and pay:
```
#TRANS 2641 {} 304518.96    // Deductible input VAT
```

### OUTPUT VAT (Utgående moms - 2611):
When you SELL to customers:

**Example: Selling rings for 50 SEK each (100 pcs)**
```
#VER A XXX 20260425 "Försäljning ringar - 100 st"
{
   #TRANS 1940 {} 6250.00        // Cash received (incl VAT)
   #TRANS 3051 {} -5000.00       // Sales revenue (excl VAT)
   #TRANS 2611 {} -1250.00       // Output VAT 25%
}

#VER A XXX 20260425 "COGS - ringar"
{
   #TRANS 4110 {} 1902.00        // Cost (100 × 19.02 SEK)
   #TRANS 1460 {} -1902.00       // Reduce inventory
}
```

**VAT Flow:**
- Input VAT (2641): +304,518.96 SEK → Claim from Skatteverket
- Output VAT (2611): -1,250.00 SEK → Pay to Skatteverket
- Net VAT position: 304,518.96 - 1,250.00 = 303,268.96 SEK to reclaim

---

## 📋 INVENTORY DATABASE (CSV)

SKU,Product,Account,Qty,Unit_SEK,Total_SEK,Resellable
CHILD-CLOTH-001,Children's clothing,1460,2965,9.60,28464.00,YES
WOMEN-OUTWEAR-001,Women's outerwear,1460,1107,46.66,51648.19,YES
MEN-MIX-001,Men's mixed clothing,1460,1431,46.08,65940.48,YES
WOMEN-TROUSERS-001,Women's trousers,1460,136,25.06,3407.62,YES
WOMEN-DRESS-001,Women's dresses,1460,223,64.61,14407.58,YES
WOMEN-MIX-001,Women's mixed clothing,1460,350,44.74,15657.60,YES
SOCKS-001,Socks,1460,5100,0.96,4896.00,YES
SCARVES-HIJ-001,Scarves/Hijab,1460,2141,11.61,24869.86,YES
HANDBAGS-001,Handbags,1460,1190,34.18,40669.44,YES
FOOTWEAR-001,Footwear,1460,912,18.91,17247.74,YES
RINGS-001,Rings,1460,3784,19.01,71926.27,YES
EARRINGS-001,Earrings,1460,3603,11.91,42889.71,YES
NECKLACE-BRAC-001,Necklaces & Bracelets,1460,2933,36.49,106995.84,YES
JEWELRY-SETS-001,Jewellery sets,1460,240,41.57,9976.32,YES
JEWELRY-MIX-001,Mixed jewellery,1460,1260,35.71,44996.32,YES
DOLLS-TOYS-001,Dolls & toys,1460,162,67.01,10855.30,YES
RC-TOYS-001,Remote control toys,1460,336,112.01,37642.75,YES
TOY-SHOOTING-001,Plastic toy shooting,1460,300,46.94,14083.20,YES
EARPHONES-001,Earphones,1460,1500,120.00,180000.00,YES
RING-BOXES-001,Ring boxes,5460,9886,11.14,110090.50,NO
GIFT-WRAP-001,Paper packaging,5460,8360,8.83,73835.52,NO
METAL-FIXTURE-001,Metal store fixtures,1220,193,403.21,77817.60,NO
DISPLAY-SCREEN-001,Display screens,1220,4,7200.00,28800.00,NO
CONVEYOR-SYSTEM-001,Roller conveyor,1220,10,2736.00,27360.00,NO
IRON-CABINET-001,Iron display cabinet,1220,2,10560.00,21120.00,NO
MANNEQUIN-001,Plastic mannequins,1220,10,3427.20,34272.00,NO
JEWELRY-DISPLAY-001,Jewelry display stand,1220,1410,41.28,58204.80,NO

---

## ✅ VERIFICATION CHECKLIST

Before adding to SIE:
- [ ] Confirm payment date from Wise USD (1942) statement
- [ ] Invoice total: $126,882.90 USD
- [ ] Exchange rate: 9.6 SEK/USD
- [ ] SEK total: 1,218,075.84 SEK (EXACT - no additions)
- [ ] VAT 25%: 304,518.96 SEK
- [ ] Total payment: 1,522,594.60 SEK (invoice + VAT)

After adding:
- [ ] Debit = Credit in verification
- [ ] Account 1460: +791,575.22 SEK
- [ ] Account 1220: +247,574.40 SEK
- [ ] Account 5460: +183,926.02 SEK
- [ ] Account 2641: +304,518.96 SEK (VAT to reclaim)
- [ ] Account 1942: -1,527,594.60 SEK (payment)

---

## 🚨 CRITICAL RULES

✅ **Invoice amount ONLY** - no freight, no customs, no additions
✅ **ONE VAT calculation** - 25% on 1,218,075.84 SEK
✅ **Cash basis** - record when actually paid
✅ **Both VAT sides** - Input (2641) when buying, Output (2611) when selling
✅ **Account mapping** - 1460 (inventory), 1220 (equipment), 5460 (packaging)

---

**Status:** ✅ CORRECTED - SIMPLE INVOICE PROCESSING  
**No freight/customs added**  
**Invoice price = Final cost**  
**VAT shown both directions**
