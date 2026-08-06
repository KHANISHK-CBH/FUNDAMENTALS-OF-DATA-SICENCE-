import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Kaggle dataset
df = pd.read_csv('house_prices.csv')
col = 'SalePrice'

# Outlier filtering using IQR
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

df_clean = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

print("=" * 40)
print("     PROBLEM 7: BEFORE VS AFTER OUTLIER PLOTS")
print("=" * 40)
print(f"\nOriginal Rows: {len(df)} | Cleaned Rows: {len(df_clean)}")

# Plot 2x2 grid comparing distributions
fig, axes = plt.subplots(2, 2, figsize=(11, 7))

# Before Removal
sns.histplot(df[col], ax=axes[0, 0], kde=True, color='crimson').set_title("Histogram (Before)")
sns.boxplot(x=df[col], ax=axes[0, 1], color='crimson').set_title("Box Plot (Before)")

# After Removal
sns.histplot(df_clean[col], ax=axes[1, 0], kde=True, color='seagreen').set_title("Histogram (After)")
sns.boxplot(x=df_clean[col], ax=axes[1, 1], color='seagreen').set_title("Box Plot (After)")

plt.suptitle("Distribution Comparison (Before vs After Outlier Removal)", fontsize=14)
plt.tight_layout()
plt.show()