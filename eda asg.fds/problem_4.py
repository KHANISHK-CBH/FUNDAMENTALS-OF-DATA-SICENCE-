import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Kaggle DS Salaries dataset
df = pd.read_csv('ds_salaries.csv')

plt.figure(figsize=(6, 6))
sns.boxplot(y=df['salary_in_usd'], color='lightgreen')
plt.title("Box Plot of Salary Data")
plt.ylabel("Salary (USD)")
plt.tight_layout()

# IQR calculations for outlier detection
Q1 = df['salary_in_usd'].quantile(0.25)
Q3 = df['salary_in_usd'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + (1.5 * IQR)
outliers = df[df['salary_in_usd'] > upper_bound]

print("=" * 40)
print("     PROBLEM 4: SALARY OUTLIERS")
print("=" * 40)
print(f"\nUpper Outlier Threshold: ${upper_bound:,.2f}")
print(f"Total Outliers Identified: {len(outliers)}")

plt.show()