#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FULL LUNAR BANK Q1 2026 AUDIT
Analyze every transaction to categorize properly with MOMS separation
"""

import csv
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

def parse_lunar_date(date_str):
    """Parse DD-MM-YYYY format"""
    return datetime.strptime(date_str, "%d-%m-%Y")

def main():
    lunar_csv = Path("source_csv/Lunar Bank/Lunar export.csv")
    
    transactions = []
    sales_income = Decimal("0")
    fees = Decimal("0")
    transfers_out = Decimal("0")
    expenses = Decimal("0")
    returns = Decimal("0")
    owner_transactions = Decimal("0")
    
    print("=" * 80)
    print("LUNAR BANK Q1 2026 - FULL TRANSACTION AUDIT")
    print("=" * 80)
    print()
    
    with open(lunar_csv, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            date_str = row['Date']
            text = row['Text']
            amount = Decimal(row['Amount'].replace(',', '.'))
            balance = Decimal(row['Balance'].replace(',', '.'))
            note = row.get('Note', '')
            
            date = parse_lunar_date(date_str)
            
            # Categorize
            category = "Unknown"
            account = "????"
            moms_rate = None
            moms_amount = Decimal("0")
            base_amount = amount
            
            if text == "Fee":
                category = "Bank Fee"
                account = "6570"
                fees += amount
                
            elif "Transfer" in text or "Till 1930" in text or "To 1930" in text:
                category = "Transfer to Marginalen"
                account = "1930"
                transfers_out += amount
                
            elif "2893" in text or "återbetalning" in text.lower():
                category = "Owner/Shareholder Transaction"
                account = "2893"
                owner_transactions += amount
                
            elif "Retur" in text or "refund" in text.lower():
                category = "Sales Return/Refund"
                account = "3001"
                returns += amount
                
            elif "STRIPE" in text:
                category = "Stripe Sales Income"
                account = "3001"
                sales_income += amount
                # Split out 25% MOMS
                moms_rate = 25
                base_amount = amount / Decimal("1.25")
                moms_amount = amount - base_amount
                
            elif "Everygreen" in text or "seaport" in text:
                category = "Freight/Shipping"
                account = "5710"
                expenses += amount
                
            elif "TWILIO" in text:
                category = "SaaS/Software"
                account = "5420"
                expenses += amount
                
            elif "Swish" in text and "enrollment" in text:
                category = "Bank Fee"
                account = "6570"
                fees += amount
                
            elif "Lunar Plan" in text:
                category = "Bank Plan Fee"
                account = "6570"
                fees += amount
                
            elif amount > 0:
                # Positive = Sales income from customer
                category = "Customer Sales"
                account = "3001"
                sales_income += amount
                # Assume 25% MOMS
                moms_rate = 25
                base_amount = amount / Decimal("1.25")
                moms_amount = amount - base_amount
            
            transactions.append({
                'date': date,
                'text': text,
                'amount': amount,
                'category': category,
                'account': account,
                'moms_rate': moms_rate,
                'moms_amount': moms_amount,
                'base_amount': base_amount,
                'balance': balance
            })
    
    # Sort by date
    transactions.sort(key=lambda x: x['date'])
    
    # Print transactions
    print(f"{'Date':<12} {'Category':<25} {'Account':<8} {'Amount':>12} {'MOMS%':<6} {'MOMS':>10} {'Base':>12} {'Description':<40}")
    print("-" * 140)
    
    for tx in transactions:
        moms_str = f"{tx['moms_rate']}%" if tx['moms_rate'] else ""
        moms_amt = f"{tx['moms_amount']:,.2f}" if tx['moms_amount'] else ""
        base_amt = f"{tx['base_amount']:,.2f}" if tx['base_amount'] != tx['amount'] else ""
        
        print(f"{tx['date'].strftime('%Y-%m-%d'):<12} {tx['category']:<25} {tx['account']:<8} {tx['amount']:>12,.2f} {moms_str:<6} {moms_amt:>10} {base_amt:>12} {tx['text'][:40]:<40}")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Sales Income (gross with MOMS):     {sales_income:>15,.2f} SEK")
    print(f"Sales Returns/Refunds:              {returns:>15,.2f} SEK")
    print(f"Bank Fees:                          {fees:>15,.2f} SEK")
    print(f"Expenses (Freight, SaaS):           {expenses:>15,.2f} SEK")
    print(f"Transfers to Marginalen (1930):     {transfers_out:>15,.2f} SEK")
    print(f"Owner Transactions (2893):          {owner_transactions:>15,.2f} SEK")
    print()
    print(f"Total Transactions: {len(transactions)}")
    print()
    
    # Calculate MOMS summary
    total_moms_out = sum(tx['moms_amount'] for tx in transactions if tx['moms_amount'] > 0)
    print(f"Total MOMS (Utgående moms 25%):     {total_moms_out:>15,.2f} SEK")
    print()
    
    # Look for potential IT expenses
    print("=" * 80)
    print("POTENTIAL IT/EQUIPMENT EXPENSES (mobiles, laptops)?")
    print("=" * 80)
    print("Searching for large expenses or IT-related terms...")
    print()
    
    it_candidates = []
    for tx in transactions:
        # Look for large expenses or IT-related terms
        if tx['amount'] < -500 or any(term in tx['text'].lower() for term in ['it', 'tech', 'laptop', 'mobile', 'phone', 'computer']):
            it_candidates.append(tx)
    
    if it_candidates:
        for tx in it_candidates:
            print(f"{tx['date'].strftime('%Y-%m-%d')}: {tx['text']:<50} {tx['amount']:>12,.2f} SEK")
    else:
        print("❌ NO large IT expenses found in Lunar Bank Q1 2026")
        print("   (Looking for transactions > -500 SEK or IT-related terms)")
    
    print()
    print("=" * 80)
    print("IMPORTANT: Snabbgross food purchases (3863 kr with 6% MOMS)?")
    print("=" * 80)
    print("User mentioned cash purchases (1910) not in Lunar Bank!")
    print("These need to be added manually if paid from cash (1910)")
    print()

if __name__ == "__main__":
    main()
