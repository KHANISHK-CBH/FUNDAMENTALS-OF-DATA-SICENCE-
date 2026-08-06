import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Kaggle House Prices dataset
df = pd.read_csv('house_prices.csv')

plt.figure(figsize=(9, 5))
sns.histplot(df['SalePrice'], kde=True, color='teal')
plt.title("Distribution of House Prices")
plt.xlabel("Sale Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()

# Calculate skewness
skewness = df['SalePrice'].skew()

print("=" * 40)
print("     PROBLEM 3: HOUSE PRICES ANALYSIS")
print("=" * 40)
print(f"\nSalePrice Skewness: {skewness:.2f}")

if abs(skewness) < 0.5:
    print("Conclusion: The house price data is roughly Normally Distributed.")
elif skewness > 0.5:
    print("Conclusion: The house price data is Right-Skewed (Positively Skewed).")
else:
    print("Conclusion: The house price data is Left-Skewed (Negatively Skewed).")

plt.show()