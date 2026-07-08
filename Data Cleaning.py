import pandas as pd

# 1. Load the raw dataset using read_excel instead of read_csv
file_path = 'Dataset for Data Analytics.xlsx' # Update this if your file name is different
df = pd.read_excel(file_path)

print(f"Initial row count: {len(df)}")

# --- PHASE 2: THE INTEGRITY AUDIT ---
initial_rows = len(df)
df = df.drop_duplicates(subset=['OrderID'])
duplicates_removed = initial_rows - len(df)

print(f"Action: Removed {duplicates_removed} duplicate OrderID records.")

# --- PHASE 3: SPEAK ONE LANGUAGE (DATES) ---
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

print("Action: Standardized Date column to ISO 8601 format (YYYY-MM-DD).")

# --- PHASE 3: SPEAK ONE LANGUAGE (STANDARDIZATION) ---

text_columns = ['ShippingAddress', 'PaymentMethod', 'Product', 'OrderStatus']
for col in text_columns:
    df[col] = df[col].str.strip().str.title()


df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)

print("Action: Trimmed whitespace, enforced Title Case on text columns, and rounded currency to 2 decimals.")


# --- PHASE 4: STRATEGIC IMPUTATION (THE MISSING VALUE AUDIT) ---
print("\n--- MISSING VALUES AUDIT ---")
missing_data = df.isnull().sum()
columns_with_missing = missing_data[missing_data > 0]

if not columns_with_missing.empty:
    print(columns_with_missing)
else:
    print("No missing values found!")

# PHASE 4: STRATEGIC IMPUTATION

df['CouponCode'] = df['CouponCode'].fillna('NONE')

print("Action: Imputed 309 missing CouponCode values with 'NONE'.")

# Final verification to prove 0 missing values remain
final_missing = df.isnull().sum().sum()
print(f"Final Missing Values Audit: {final_missing} missing values remaining.")

# --- PHASE 5: EXPORT THE CLEAN DATA ---

export_name = 'Cleaned_Dataset_Project1.xlsx'
df.to_excel(export_name, index=False)

print(f"\nSUCCESS! Clean dataset saved as: {export_name}")