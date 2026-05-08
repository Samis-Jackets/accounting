#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Visma import errors:
1. Add missing account 4580
2. Remove VER A 130 (empty verification)
3. Add missing opening balance for 2098 (2025 result)
4. Renumber verifications after removed VER A 130
"""

from pathlib import Path
import re

def main():
    master_file = Path("MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    
    print("=" * 80)
    print("FIXING VISMA IMPORT ERRORS")
    print("=" * 80)
    print()
    
    # Read the file
    with open(master_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    in_ver_a130 = False
    skip_count = 0
    ver_number_adjust = False
    
    for i, line in enumerate(lines):
        # Add account 4580 after account 3994 (in the KONTO section)
        if line.startswith('#KONTO 3994'):
            new_lines.append(line)
            new_lines.append('#KONTO 4580 "Varor för återförsäljning - livsmedel"\n')
            print("✅ Added #KONTO 4580 after account 3994")
            continue
        
        # Add opening balance 2098 after #IB 0 2093
        if line.startswith('#IB 0 2093'):
            new_lines.append(line)
            new_lines.append('#IB 0 2098 303561.63\n')
            print("✅ Added #IB 0 2098 303561.63 (2025 result transferred to equity)")
            continue
        
        # Skip VER A 130 and its content
        if line.startswith('#VER A 130 '):
            in_ver_a130 = True
            skip_count = 1
            ver_number_adjust = True
            print("✅ Removing VER A 130 (empty verification)")
            continue
        
        if in_ver_a130:
            skip_count += 1
            if line.strip() == '}':
                in_ver_a130 = False
            continue
        
        # Renumber verifications after A 130
        if ver_number_adjust and line.startswith('#VER A '):
            match = re.match(r'#VER A (\d+) ', line)
            if match:
                old_num = int(match.group(1))
                if old_num > 130:
                    new_num = old_num - 1
                    line = line.replace(f'#VER A {old_num} ', f'#VER A {new_num} ', 1)
        
        new_lines.append(line)
    
    print(f"   Removed {skip_count} lines (VER A 130)")
    print()
    
    # Write back
    with open(master_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    # Verify
    with open(master_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    konto_4580 = '#KONTO 4580' in content
    ib_2098 = '#IB 0 2098' in content
    ver_a130_gone = '#VER A 130 ' not in content
    ver_count = content.count('\n#VER A ')
    
    print("=" * 80)
    print("VERIFICATION")
    print("=" * 80)
    print(f"✅ Account 4580 defined: {konto_4580}")
    print(f"✅ Opening balance 2098 added: {ib_2098}")
    print(f"✅ VER A 130 removed: {ver_a130_gone}")
    print(f"✅ Total verifications now: {ver_count}")
    print()
    
    # Calculate new opening balance total
    ib_lines = [l for l in new_lines if l.startswith('#IB')]
    ib_total = 0
    for ib_line in ib_lines:
        parts = ib_line.split()
        ib_total += float(parts[3])
    
    print(f"📊 Opening balance total: {ib_total:.2f} SEK")
    if abs(ib_total) < 0.01:
        print("   ✅ BALANCED!")
    else:
        print(f"   ⚠️  Still imbalanced by {ib_total:.2f} SEK")
    
    print()
    print("=" * 80)
    print("File ready for Visma: MASTER_Q1_2026_CORRECTED_CASH_BASIS.se")
    print("=" * 80)

if __name__ == "__main__":
    main()
