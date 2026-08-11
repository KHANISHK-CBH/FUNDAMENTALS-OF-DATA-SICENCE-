import pandas as pd

# Load Kaggle Employee dataset
df = pd.read_csv('employee_data.csv')

print("=" * 40)
print("     PROBLEM 1: EMPLOYEE DATASET SUMMARY")
print("=" * 40)

print(f"\nNumber of Rows:    {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Statistical Summary ---")
print(df.describe(include='all'))