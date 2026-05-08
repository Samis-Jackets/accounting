import re
from decimal import Decimal

# Test parsing
with open(r'Q1_2026_PERIOD_2026-01_TO_2026-03\MASTER_Q1_2026_CORRECTED_CASH_BASIS.se', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print()

# Test Stripe EUR line
line_113 = lines[113]
print("Line 113:", repr(line_113))

ver_match = re.match(r'#VER\s+(\w+)\s+(\d+)\s+(\d{8})\s+"Stripe\s+([A-Z0-9]+)\s+\[WISE_EUR\]"', line_113)
print("Match result:", ver_match)
if ver_match:
    print("Groups:", ver_match.groups())

# Read next few lines
print("\nNext 5 lines:")
for i in range(114, 119):
    print(f"Line {i}: {repr(lines[i])}")
