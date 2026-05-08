#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Snabbgross purchase to Q1 2026 SE file
March 19, 2026: 3,863 SEK cash purchase with 6% MOMS
"""

from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP

def main():
    se_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    
    # Read the file
    with open(se_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Calculate MOMS
    total = Decimal("3863.00")
    base = (total / Decimal("1.06")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    moms = total - base
    
    print(f"Snabbgross purchase calculation:")
    print(f"  Total with 6% MOMS: {total} SEK")
    print(f"  Base amount: {base} SEK")
    print(f"  MOMS 6%: {moms} SEK")
    print()
    
    # New verification to insert after VER A 456 (March 19)
    new_ver = f'''#VER A 457 20260319 "Snabbgross - Food/Beverage Cash Purchase [KASSA]"
{{
   #TRANS 1910 {{}} -3863.00
   #TRANS 4580 {{}} {base}
   #TRANS 2641 {{}} {moms}
}}
'''
    
    # Find insertion point (after VER A 456)
    insert_index = None
    for i, line in enumerate(lines):
        if '#VER A 456 20260319' in line:
            # Find the closing brace of this verification
            for j in range(i+1, len(lines)):
                if lines[j].strip() == '}':
                    insert_index = j + 1
                    break
            break
    
    if insert_index is None:
        print("ERROR: Could not find VER A 456")
        return
    
    print(f"Inserting new verification at line {insert_index + 1}")
    print()
    
    # Insert the new verification
    lines.insert(insert_index, new_ver)
    
    # Renumber all subsequent verifications (457 -> 458, 458 -> 459, etc.)
    print("Renumbering subsequent verifications...")
    renumber_count = 0
    for i in range(insert_index + 1, len(lines)):
        line = lines[i]
        if line.startswith('#VER A '):
            parts = line.split()
            if len(parts) >= 3:
                old_num = int(parts[2])
                if old_num >= 457:
                    new_num = old_num + 1
                    lines[i] = line.replace(f'#VER A {old_num} ', f'#VER A {new_num} ')
                    renumber_count += 1
    
    print(f"Renumbered {renumber_count} verifications")
    print()
    
    # Write back
    output_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS_WITH_SNABBGROSS.se")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✅ Updated SE file saved as: {output_file}")
    print()
    print("New verification added:")
    print(new_ver)
    
    # Count total verifications
    total_vers = sum(1 for line in lines if line.startswith('#VER A '))
    print(f"Total verifications: {total_vers} (was 525, now 526)")

if __name__ == "__main__":
    main()
