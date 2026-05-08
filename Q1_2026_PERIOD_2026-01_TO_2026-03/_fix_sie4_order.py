#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix SIE4 tag order: #KONTO must come BEFORE #IB
Correct order: #RAR → #KONTO → #IB → #VER
"""

from pathlib import Path

def main():
    master_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    
    print("=" * 80)
    print("FIXING SIE4 TAG ORDER")
    print("=" * 80)
    print()
    print("Issue: #IB entries are BEFORE #KONTO entries")
    print("Fix: Move #KONTO entries BEFORE #IB entries")
    print()
    
    # Read the file
    with open(master_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Separate sections
    header_lines = []  # Everything up to and including #RAR
    ib_lines = []      # All #IB entries
    konto_lines = []   # All #KONTO entries
    ver_lines = []     # All #VER entries and other content
    
    current_section = 'header'
    
    for line in lines:
        if line.startswith('#IB'):
            ib_lines.append(line)
            current_section = 'ib'
        elif line.startswith('#KONTO'):
            konto_lines.append(line)
            current_section = 'konto'
        elif line.startswith('#VER'):
            ver_lines.append(line)
            current_section = 'ver'
        else:
            if current_section == 'header':
                header_lines.append(line)
            elif current_section == 'ver' or current_section == 'konto':
                ver_lines.append(line)
    
    print(f"Header lines: {len(header_lines)}")
    print(f"#KONTO entries: {len(konto_lines)}")
    print(f"#IB entries: {len(ib_lines)}")
    print(f"#VER and other: {len(ver_lines)}")
    print()
    
    # Reconstruct in correct order
    new_lines = []
    new_lines.extend(header_lines)  # Header + #RAR
    new_lines.extend(konto_lines)   # #KONTO definitions
    new_lines.extend(ib_lines)      # #IB opening balances
    new_lines.extend(ver_lines)     # #VER verifications
    
    # Write back
    with open(master_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("✅ File corrected with proper SIE4 tag order:")
    print("   1. Header (#FLAGGA, #PROGRAM, #FORMAT, #GEN, #SIETYP, #FNAMN, #ORGNR, #KPTYP)")
    print("   2. #RAR (fiscal year definitions)")
    print("   3. #KONTO (account definitions)")
    print("   4. #IB (opening balances)")
    print("   5. #VER (verifications)")
    print()
    print("=" * 80)
    print("File ready for Visma: MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    print("=" * 80)

if __name__ == "__main__":
    main()
