#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove duplicate #IB entries from MASTER file
Keep only the first set (lines 11-29)
"""

from pathlib import Path

def main():
    master_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    
    print("=" * 80)
    print("REMOVING DUPLICATE #IB ENTRIES")
    print("=" * 80)
    print()
    
    # Read the file
    with open(master_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find first #IB and last #IB in the header section
    first_ib_index = None
    last_header_ib_index = None
    first_konto_index = None
    
    for i, line in enumerate(lines):
        if line.startswith('#IB') and first_ib_index is None:
            first_ib_index = i
        if line.startswith('#KONTO'):
            first_konto_index = i
            break
        if line.startswith('#IB'):
            last_header_ib_index = i
    
    print(f"First #IB at line: {first_ib_index + 1}")
    print(f"Last header #IB at line: {last_header_ib_index + 1}")
    print(f"First #KONTO at line: {first_konto_index + 1}")
    print()
    
    # Remove all #IB lines AFTER the first #KONTO
    new_lines = []
    ib_removed_count = 0
    
    for i, line in enumerate(lines):
        # Keep everything before first_konto_index
        if i < first_konto_index:
            new_lines.append(line)
        # After first_konto_index, skip #IB lines
        elif line.startswith('#IB'):
            ib_removed_count += 1
            continue
        else:
            new_lines.append(line)
    
    print(f"Removed {ib_removed_count} duplicate #IB entries from transaction sections")
    print()
    
    # Write back
    with open(master_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    # Verify
    with open(master_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    final_ib_count = content.count('\n#IB')
    final_ver_count = content.count('\n#VER A')
    
    print(f"✅ File cleaned!")
    print()
    print(f"Final #IB entries: {final_ib_count}")
    print(f"Final verifications: {final_ver_count}")
    print()
    print("=" * 80)
    print("File ready for Visma: MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    print("=" * 80)

if __name__ == "__main__":
    main()
