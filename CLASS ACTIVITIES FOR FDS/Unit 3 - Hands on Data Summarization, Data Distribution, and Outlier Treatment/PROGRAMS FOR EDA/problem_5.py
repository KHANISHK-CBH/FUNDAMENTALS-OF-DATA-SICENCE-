import pandas as pd

# Load Kaggle Student Marks dataset
df = pd.read_csv('StudentsPerformance.csv')
marks = df['math score']

Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[(marks < lower_bound) | (marks > upper_bound)]

print("=" * 40)
print("     PROBLEM 5: MARKS IQR OUTLIER DETECTION")
print("=" * 40)
print(f"\nQ1 (25th Percentile): {Q1}")
print(f"Q3 (75th Percentile): {Q3}")
print(f"IQR:                 {IQR}")
print(f"Lower Bound:         {lower_bound}")
print(f"Upper Bound:         {upper_bound}")
print(f"\nTotal Outliers Detected: {len(outliers)}")
print("\nOutlier Records:")
print(outliers[['math score']])