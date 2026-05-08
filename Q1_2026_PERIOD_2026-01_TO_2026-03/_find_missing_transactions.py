#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find missing transactions - detailed comparison
"""

from pathlib import Path
import re

def extract_transactions(filepath):
    """Extract all VER lines with date and description"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
    
    # Pattern: #VER A number date "description"
    pattern = r'#VER\s+A\s+\d+\s+(\d{8})\s+"([^"]+)"'
    matches = re.findall(pattern, content)
    return [(date, desc) for date, desc in matches]

def main():
    base = Path(".")
    
    print("=" * 80)
    print("FINDING MISSING TRANSACTIONS")
    print("=" * 80)
    print()
    
    # Check USD
    print("🔍 WISE_USD Missing Transactions:")
    print("-" * 80)
    usd_standalone = extract_transactions(base / "source_csv/wise/usd/WISE_USD_STANDALONE.se")
    master = extract_transactions(base / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    master_usd = [(date, desc) for date, desc in master if "[WISE_USD]" in desc]
    
    for date, desc in usd_standalone:
        # Check if this transaction is in master (by date and partial description match)
        desc_clean = desc.replace("Card ", "").replace("Sent money to ", "")[:30]
        found = any(desc_clean in m_desc for m_date, m_desc in master_usd if m_date == date)
        if not found:
            print(f"❌ {date}: {desc}")
    
    print()
    
    # Check EUR
    print("🔍 WISE_EUR Missing Transactions:")
    print("-" * 80)
    eur_standalone = extract_transactions(base / "source_csv/wise/eur/WISE_EUR_STANDALONE.se")
    master_eur = [(date, desc) for date, desc in master if "[WISE_EUR]" in desc]
    
    for date, desc in eur_standalone:
        desc_clean = desc.replace("Card ", "").replace("Stripe ", "")[:30]
        found = any(desc_clean in m_desc for m_date, m_desc in master_eur if m_date == date)
        if not found:
            print(f"❌ {date}: {desc}")
    
    print()
    
    # Check SKATTEVERKET
    print("🔍 SKATTEVERKET Missing Transactions:")
    print("-" * 80)
    skv_standalone = extract_transactions(base / "source_csv/Skattverket/SKATTEVERKET_STANDALONE.se")
    master_skv = [(date, desc) for date, desc in master if "SKATTEVERKET" in desc or "SKV" in desc]
    
    for date, desc in skv_standalone:
        found = any(desc[:20] in m_desc for m_date, m_desc in master_skv if m_date == date)
        if not found:
            print(f"❌ {date}: {desc}")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()
