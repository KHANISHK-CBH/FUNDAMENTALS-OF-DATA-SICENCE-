import numpy as np
import pandas as pd

# Sample data with missing entries
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 45000],
}
df = pd.DataFrame(data)

# 1. Check for missing values
print("Missing count:\n", df.isnull().sum())

# 2. Fill missing Age with the column median
df['Age'] = df['Age'].fillna(df['Age'].median())

# 3. Drop rows where Salary is missing
df = df.dropna(subset=['Salary'])
print("\nCleaned DataFrame:\n", df)