import pandas as pd
import re

print("--- DECODELABS: QUALITY ASSURANCE AUDIT ---\n")

# 1. Load the cleaned dataset
file_path = 'Cleaned_Dataset_Project1.csv' 
df = pd.read_csv(file_path)

# --- AUDIT 1: The Verification Gate (Duplicates) ---
duplicates = df.duplicated(subset=['OrderID']).sum()
print(f"[1] Duplicate 'OrderID' Check: {duplicates} found.")
if duplicates > 0:
    print("    -> WARNING: The Verification Gate failed. Duplicates exist!")

# --- AUDIT 2: The Missing Value Audit ---
missing_total = df.isnull().sum().sum()
print(f"[2] Missing Values Check: {missing_total} missing cells found.")
if missing_total > 0:
    print("    -> WARNING: The following columns still have missing data:")
    missing_cols = df.isnull().sum()
    print(missing_cols[missing_cols > 0])

# --- AUDIT 3: Strict Date Formatting (ISO 8601: YYYY-MM-DD) ---
invalid_dates = df[~df['Date'].astype(str).str.match(r'^\d{4}-\d{2}-\d{2}$')]
print(f"[3] Date Format Check: {len(invalid_dates)} invalid dates found.")

#  AUDIT 4: The Whitespace & Text Standardization Check 
untrimmed_issues = 0
text_columns = ['ShippingAddress', 'PaymentMethod', 'Product', 'OrderStatus']

for col in text_columns:
    # Compare original string to a stripped version of the string
    has_whitespace = (df[col].astype(str) != df[col].astype(str).str.strip()).sum()
    untrimmed_issues += has_whitespace

print(f"[4] Whitespace & Text Check: {untrimmed_issues} un-trimmed text cells found.")

print("\n AUDIT COMPLETE ")
if duplicates == 0 and missing_total == 0 and len(invalid_dates) == 0 and untrimmed_issues == 0:
    print("RESULT: PASS. Your dataset is 100% clean and verified!")
else:
    print("RESULT: FAIL. Review the warnings above and re-run your cleaning script.")