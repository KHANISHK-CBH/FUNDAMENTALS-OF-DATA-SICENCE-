import matplotlib.pyplot as plt
import pandas as pd

# Create sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}
df = pd.DataFrame(data)

print("\n--- 4. PLOTTING ---")
print("Opening plots... (Close the plot windows to finish execution)")

# Bar chart of students' marks
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'])
plt.title('Student Marks')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot average marks by department
grouped_df = df.groupby('Department')['Marks'].mean()
grouped_df.plot(kind='bar')
plt.title('Average Marks by Department')
plt.xlabel('Department')
plt.ylabel('Average Marks')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()