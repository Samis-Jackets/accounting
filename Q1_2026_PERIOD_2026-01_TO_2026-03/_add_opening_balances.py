#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add opening balances (#IB) to MASTER Q1 2026 file from 2025 closing balances
"""

from pathlib import Path

def main():
    # Opening balances from 2025 ending balances (#UB)
    opening_balances = [
        "#IB 0 1220 49170.68",
        "#IB 0 1240 27500.00",
        "#IB 0 1460 566933.00",
        "#IB 0 1580 39934.97",
        "#IB 0 1630 103.00",
        "#IB 0 1910 0.92",
        "#IB 0 1930 42490.75",
        "#IB 0 1941 -0.55",
        "#IB 0 1942 4503.41",
        "#IB 0 1947 14591.99",
        "#IB 0 1948 0.17",
        "#IB 0 2091 -2511.47",
        "#IB 0 2093 -1.00",
        "#IB 0 2441 610300.17",
        "#IB 0 2448 -0.92",
        "#IB 0 2510 22940.00",
        "#IB 0 2641 1053.60",
        "#IB 0 2650 -81643.00",
        "#IB 0 2893 -1598927.35",
    ]
    
    master_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    
    print("=" * 80)
    print("ADDING OPENING BALANCES (#IB) TO MASTER Q1 2026 FILE")
    print("=" * 80)
    print()
    
    # Read the file
    with open(master_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where to insert #IB lines (after #RAR -1 and before first #KONTO)
    insert_index = None
    for i, line in enumerate(lines):
        if line.startswith('#KONTO'):
            insert_index = i
            break
    
    if insert_index is None:
        print("ERROR: Could not find #KONTO line")
        return
    
    print(f"Inserting {len(opening_balances)} opening balance entries at line {insert_index + 1}")
    print()
    
    # Insert opening balances
    for ib_line in reversed(opening_balances):
        lines.insert(insert_index, ib_line + '\n')
    
    # Write back
    output_file = Path("MASTER_Q1_2026_WITH_OPENING_BALANCES.se")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✅ File created: {output_file}")
    print()
    print("Opening balances added:")
    for ib in opening_balances:
        parts = ib.split()
        account = parts[2]
        amount = parts[3]
        print(f"  Account {account}: {amount}")
    
    print()
    print("=" * 80)
    print("NEXT STEP: Test import this file in Visma")
    print("=" * 80)

if __name__ == "__main__":
    main()
