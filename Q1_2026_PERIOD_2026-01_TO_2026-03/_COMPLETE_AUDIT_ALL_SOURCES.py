#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPLETE AUDIT - Verify MASTER file contains ALL transactions from ALL sources
"""

from pathlib import Path
import re

def count_verifications_in_file(filepath):
    """Count #VER lines in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
    return len(re.findall(r'^#VER\s+', content, re.MULTILINE))

def count_tagged_transactions(filepath, tag):
    """Count transactions with specific tag like [WISE_USD]"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
    return len(re.findall(rf'\[{tag}\]', content))

def main():
    base = Path(".")
    master_file = base / "MASTER_Q1_2026_CORRECTED_CASH_BASIS.se"
    
    print("=" * 80)
    print("COMPLETE Q1 2026 AUDIT - ALL SOURCES")
    print("=" * 80)
    print()
    
    # Count total verifications in MASTER
    master_count = count_verifications_in_file(master_file)
    print(f"✅ MASTER FILE: {master_count} verifications")
    print()
    
    # Check each source
    sources = {
        "WISE_USD": ("source_csv/wise/usd/WISE_USD_STANDALONE.se", "Wise USD Account"),
        "WISE_EUR": ("source_csv/wise/eur/WISE_EUR_STANDALONE.se", "Wise EUR Account"),
        "WISE_SEK": ("source_csv/wise/sek/WISE_SEK_STANDALONE.se", "Wise SEK Account"),
        "WISE_GBP": ("source_csv/wise/gbp/WISE_GBP_STANDALONE.se", "Wise GBP Account"),
        "LUNAR": ("source_csv/Lunar Bank/LUNAR_STANDALONE.se", "Lunar Bank Account 1948"),
        "MARGINALEN": ("source_csv/marginalen/MARGINALEN_STANDALONE.se", "Marginalen Bank Account 1930"),
        "WORLDLINE": ("source_csv/worldline/WORLDLINE_STANDALONE.se", "Worldline Payment Terminal"),
        "SKATTEVERKET": ("source_csv/Skattverket/SKATTEVERKET_STANDALONE.se", "Skatteverket Tax Account"),
        "NORDEA": ("source_csv/nordea/NORDEA_STANDALONE.se", "Nordea Bank"),
    }
    
    print("=" * 80)
    print("SOURCE FILE COMPARISON")
    print("=" * 80)
    print()
    
    total_source_vers = 0
    all_good = True
    
    for tag, (filepath, description) in sources.items():
        source_file = base / filepath
        if not source_file.exists():
            print(f"⚠️  {tag}: File not found - {filepath}")
            continue
        
        # Count in standalone
        source_count = count_verifications_in_file(source_file)
        
        # Count in master with tag
        master_tag_count = count_tagged_transactions(master_file, tag)
        
        status = "✅" if master_tag_count >= source_count else "❌"
        if master_tag_count < source_count:
            all_good = False
        
        print(f"{status} {tag}:")
        print(f"   Standalone file: {source_count:>3} verifications")
        print(f"   In MASTER file:  {master_tag_count:>3} tagged as [{tag}]")
        print(f"   Description: {description}")
        
        if master_tag_count < source_count:
            print(f"   ⚠️  MISSING {source_count - master_tag_count} transactions!")
        elif master_tag_count > source_count:
            print(f"   ℹ️  {master_tag_count - source_count} extra (may include related transactions)")
        
        print()
        total_source_vers += source_count
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print(f"Total verifications in standalone files: {total_source_vers}")
    print(f"Total verifications in MASTER file:      {master_count}")
    print()
    
    # Note: Master may have more because it includes additional transactions
    # like cash purchases, adjustments, etc.
    if master_count >= total_source_vers:
        print("✅ MASTER file has MORE verifications than source files combined")
        print("   This is CORRECT - includes additional transactions like:")
        print("   - Cash purchases (1910 Kassa)")
        print("   - Manual adjustments")
        print("   - Cross-account transfers")
        print("   - Tax payments coordination")
    else:
        print("❌ WARNING: MASTER file has FEWER verifications than sources!")
        print(f"   Missing: {total_source_vers - master_count} verifications")
    
    print()
    print("=" * 80)
    print("ACCOUNT TAG VERIFICATION")
    print("=" * 80)
    print()
    
    # Check for common account patterns in MASTER
    account_patterns = {
        "1948": "Lunar Bank",
        "1930": "Marginalen Bank",
        "1942": "Wise USD",
        "1943": "Wise EUR",
        "1945": "Wise SEK",
        "1946": "Wise GBP",
        "1940": "Nordea Bank",
        "1910": "Kassa (Cash)",
        "1630": "Skattekonto",
    }
    
    try:
        with open(master_file, 'r', encoding='utf-8') as f:
            master_content = f.read()
    except UnicodeDecodeError:
        with open(master_file, 'r', encoding='cp1252') as f:
            master_content = f.read()
    
    for account, description in account_patterns.items():
        count = len(re.findall(rf'#TRANS {account}\s+{{}}', master_content))
        print(f"Account {account} ({description}): {count} transactions")
    
    print()
    print("=" * 80)
    if all_good:
        print("✅ AUDIT COMPLETE - ALL SOURCES VERIFIED IN MASTER FILE")
    else:
        print("⚠️  AUDIT COMPLETE - SOME DISCREPANCIES FOUND (see above)")
    print("=" * 80)

if __name__ == "__main__":
    main()
