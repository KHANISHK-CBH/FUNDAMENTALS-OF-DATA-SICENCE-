import pandas as pd

data = {
    'Store': ['North', 'South', 'North', 'West', 'South', 'West'],
    'Sales': [1200, 1500, 900, 1100, 1700, 1300],
    'Employees': [5, 7, 5, 4, 8, 4],
}
df = pd.DataFrame(data)

# Group by Store and calculate total sales and average employees
summary = (
    df.groupby('Store').agg({'Sales': 'sum', 'Employees': 'mean'}).reset_index()
)
print(summary)