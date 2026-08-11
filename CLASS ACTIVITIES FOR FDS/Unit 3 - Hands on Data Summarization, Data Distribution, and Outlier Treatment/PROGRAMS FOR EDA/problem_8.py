import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 40)
print("     PROBLEM 8: COMPLETE EDA PIPELINE")
print("=" * 40)

# 1. Load Dataset
df = pd.read_csv('Iris.csv')

# 2. Display Dataset Info
print("\n--- 1. DATASET INFO ---")
print(df.info())

# 3. Find Missing Values
print("\n--- 2. MISSING VALUES ---")
print(df.isnull().sum())

# 4. Descriptive Statistics
print("\n--- 3. DESCRIPTIVE STATISTICS ---")
print(df.describe())

# Select continuous numeric features
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
num_cols = [c for c in num_cols if c.lower() != 'id']

# 5. Plot Histograms
df[num_cols].hist(bins=15, figsize=(10, 6), color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Features (Before Outlier Removal)")
plt.tight_layout()
plt.show()

# 6. Plot Box Plots (Before Outliers Removed)
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[num_cols])
plt.title("Box Plots across Features (Before Outlier Removal)")
plt.tight_layout()
plt.show()

# 7. Detect & Remove Outliers Across All Numeric Columns
df_clean = df.copy()

print("\n--- 4. OUTLIER REMOVAL SUMMARY ---")
for c in num_cols:
    Q1 = df_clean[c].quantile(0.25)
    Q3 = df_clean[c].quantile(0.75)
    IQR = Q3 - Q1
    
    lb = Q1 - (1.5 * IQR)
    ub = Q3 + (1.5 * IQR)
    
    removed = len(df_clean[(df_clean[c] < lb) | (df_clean[c] > ub)])
    print(f"Outliers removed from '{c}': {removed}")
    
    df_clean = df_clean[(df_clean[c] >= lb) & (df_clean[c] <= ub)]

# Plot Box Plots (After Outliers Removed)
plt.figure(figsize=(9, 5))
sns.boxplot(data=df_clean[num_cols])
plt.title("Box Plots across Features (After Outlier Removal)")
plt.tight_layout()
plt.show()

# 8. Save Cleaned Dataset
cleaned_filename = 'Iris_Cleaned.csv'
df_clean.to_csv(cleaned_filename, index=False)
print(f"\nCleaned dataset saved as '{cleaned_filename}' in the same folder.")