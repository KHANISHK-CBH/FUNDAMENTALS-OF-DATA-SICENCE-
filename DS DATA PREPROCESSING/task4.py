import pandas as pd

# Create a sample dictionary with numeric and categorical data
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 90000, 110000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR'],
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# 1. Default describe() - Summary of numeric columns
print("--- Numeric Summary ---")
print(df.describe())

# 2. Categorical describe() - Summary of text/object columns
print("\n--- Categorical Summary ---")
print(df.describe(include='object'))