import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Evidence
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# 2. Check Data Completeness 
print("=== DATA COMPLETENESS ===")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0]) # Shows CouponCode has 309 missing values

# 3. Central Tendency 
print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].describe().T)

# 4.  IQR Method
print("\n=== OUTLIER DETECTION (TOTAL PRICE) ===")
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
print(f"Total Price Bounds: {lower_bound} to {upper_bound}")
print(f"Number of Outliers Found: {len(outliers)}")

# 5. Core Relationships 
print("\n=== CORRELATION MATRIX ===")
print(df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].corr())

# 6  Visual Evidence
plt.figure(figsize=(10, 5))
sns.histplot(df['TotalPrice'], kde=True, color='teal')
plt.title('Distribution of Total Price (The Center of Gravity Check)')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.savefig('total_price_distribution.png')
plt.close()