import pandas as pd

# Load Kaggle Sales dataset
df = pd.read_csv('sales_data.csv')

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Filter out outliers
df_clean = df[(df['Sales'] >= lower_bound) & (df['Sales'] <= upper_bound)]

print("=" * 40)
print("     PROBLEM 6: REMOVE SALES OUTLIERS")
print("=" * 40)
print(f"\nOriginal Dataset Size: {len(df)} rows")
print(f"Cleaned Dataset Size:  {len(df_clean)} rows")
print(f"Outliers Removed:      {len(df) - len(df_clean)} rows")

print("\n--- CLEANED DATASET SAMPLE (First 5 Rows) ---")
print(df_clean.head())