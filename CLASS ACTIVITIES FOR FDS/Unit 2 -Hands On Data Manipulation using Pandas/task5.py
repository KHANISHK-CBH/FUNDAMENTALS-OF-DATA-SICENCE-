import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 92, 78, 95, 88, 72, 91],
}
df = pd.DataFrame(data)

# 1. Get the top 5 rows (default behavior)
print(df.head())

# 2. Get the top 2 rows
print(df.head(2))

# 3. Get the bottom 3 rows
print(df.tail(3))