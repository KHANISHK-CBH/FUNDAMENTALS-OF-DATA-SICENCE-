import pandas as pd

# Create a sample DataFrame manually
print("--- Creating Sample DataFrame ---")
df = pd.DataFrame()
df['Name'] = ['John', 'Emma', 'Liam', 'Olivia']
df['Age'] = [20, 19, 21, 18]
df['Student'] = [True, True, False, True]
print(df, "\n")

# Add a new row to the existing DataFrame
new_row = pd.DataFrame([['Sophia', 22, False]], columns=['Name', 'Age', 'Student'])
df = pd.concat([df, new_row], ignore_index=True)
print("--- After Adding New Row ---")
print(df)
