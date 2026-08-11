import pandas as pd

# Create sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}
df = pd.DataFrame(data)

print("\n--- 3. RANKING ---")
df['Rank'] = df['Marks'].rank(ascending=False, method='dense')
print("Students with Rank:")
print(df.sort_values(by='Rank'))