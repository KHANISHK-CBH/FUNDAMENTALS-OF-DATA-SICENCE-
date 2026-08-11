import pandas as pd

# Create sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}
df = pd.DataFrame(data)

print("\n--- 2. GROUPING ---")
print("Average Marks by Department:")
grouped_df = df.groupby('Department')['Marks'].mean()
print(grouped_df)