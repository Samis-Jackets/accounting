"""
DEEP LEDGER ANALYSIS - Looking for patterns and anomalies
Analyzes Visma exported data for structural issues
"""

import pandas as pd
import re
from pathlib import Path

def analyze_huvudbok(file_path):
    """Analyze the Huvudbok (general ledger) for anomalies"""
    print("=" * 80)
    print("HUVUDBOK (GENERAL LEDGER) ANALYSIS")
    print("=" * 80)
    print()
    
    try:
        # Read with semicolon delimiter
        df = pd.read_csv(file_path, sep=';', encoding='cp1252')
        
        print(f"Total entries: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print()
        
        # Identify large cost entries
        print("🔍 LARGE COST ENTRIES (>50,000 SEK):")
        print("-" * 80)
        
        # Try to find amount columns
        for col in df.columns:
            if 'belopp' in col.lower() or any(char.isdigit() for char in str(df[col].iloc[0])):
                try:
                    # Clean and convert
                    df[col] = df[col].astype(str).str.replace(',', '.').str.replace(' ', '')
                    amounts = pd.to_numeric(df[col], errors='coerce')
                    
                    large_costs = df[amounts > 50000]
                    if len(large_costs) > 0:
                        print(f"\nColumn: {col}")
                        print(large_costs.head(20))
                except:
                    pass
        
    except Exception as e:
        print(f"ERROR: {e}")
        
def analyze_verifikationslista(file_path):
    """Analyze transaction list for patterns"""
    print("\n" + "=" * 80)
    print("VERIFIKATIONSLISTA (TRANSACTION LIST) ANALYSIS")
    print("=" * 80)
    print()
    
    try:
        df = pd.read_csv(file_path, sep=';', encoding='cp1252')
        
        print(f"Total rows: {len(df)}")
        print()
        
        # Look for specific accounts
        accounts_to_check = {
            '5460': 'Förbrukningsmaterial',
            '1460': 'Lager handelsvaror',
            '4110': 'Kostnad sålda varor',
            '2893': 'Skulder närstående'
        }
        
        for acc_no, acc_name in accounts_to_check.items():
            matches = df[df.astype(str).apply(lambda row: row.str.contains(acc_no, case=False, na=False).any(), axis=1)]
            print(f"Account {acc_no} ({acc_name}): {len(matches)} entries")
        
    except Exception as e:
        print(f"ERROR: {e}")

def analyze_resultatrakning(file_path):
    """Analyze income statement for red flags"""
    print("\n" + "=" * 80)
    print("RESULTATRÄKNING (INCOME STATEMENT) ANALYSIS")
    print("=" * 80)
    print()
    
    try:
        df = pd.read_csv(file_path, sep=';', encoding='cp1252')
        
        print("Key figures:")
        print("-" * 80)
        
        # Display the income statement
        print(df.to_string())
        print()
        
        # Calculate ratios
        print("\n🔍 RED FLAGS:")
        print("-" * 80)
        
        # Look for specific accounts
        for idx, row in df.iterrows():
            row_str = ' '.join(str(val) for val in row if pd.notna(val))
            
            if '5460' in row_str:
                print(f"✓ Found 5460 (Förbrukningsmaterial): {row_str}")
            if '4110' in row_str:
                print(f"✓ Found 4110 (COGS): {row_str}")
            if 'förlust' in row_str.lower() or 'loss' in row_str.lower():
                print(f"⚠️  Loss detected: {row_str}")
        
    except Exception as e:
        print(f"ERROR: {e}")

def analyze_balansrakning(file_path):
    """Analyze balance sheet for issues"""
    print("\n" + "=" * 80)
    print("BALANSRÄKNING (BALANCE SHEET) ANALYSIS")  
    print("=" * 80)
    print()
    
    try:
        df = pd.read_csv(file_path, sep=';', encoding='cp1252')
        
        print(df.to_string())
        print()
        
        print("\n🔍 KEY BALANCE SHEET ITEMS:")
        print("-" * 80)
        
        for idx, row in df.iterrows():
            row_str = ' '.join(str(val) for val in row if pd.notna(val))
            
            if '1460' in row_str:
                print(f"📦 Inventory (1460): {row_str}")
            if '2893' in row_str:
                print(f"💰 Related party debt (2893): {row_str}")
            if '2441' in row_str:
                print(f"💳 Supplier debt (2441): {row_str}")
        
    except Exception as e:
        print(f"ERROR: {e}")

def main():
    print("🔬 DEEP LEDGER FORENSIC ANALYSIS")
    print()
    
    base_path = Path(r"last results for all the 2025 csv")
    
    files = {
        'resultat': base_path / "Resultaträkning_20260106.csv",
        'balans': base_path / "Balansräkning_20260106.csv",
        'huvudbok': base_path / "Huvudbok_20260106.csv",
        'verifikation': base_path / "Verifikationslista_20260106.csv"
    }
    
    # Analyze each file
    if files['resultat'].exists():
        analyze_resultatrakning(files['resultat'])
    
    if files['balans'].exists():
        analyze_balansrakning(files['balans'])
    
    if files['huvudbok'].exists():
        analyze_huvudbok(files['huvudbok'])
    
    if files['verifikation'].exists():
        analyze_verifikationslista(files['verifikation'])
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
