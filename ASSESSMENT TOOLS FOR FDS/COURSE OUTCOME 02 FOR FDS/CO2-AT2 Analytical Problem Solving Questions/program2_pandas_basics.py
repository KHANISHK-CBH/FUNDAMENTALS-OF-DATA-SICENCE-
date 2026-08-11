import pandas as pd

# Creating Sample DataFrame
df = pd.DataFrame()
df['Name'] = ['John', 'Emma', 'Liam', 'Olivia']
df['Age'] = [20, 19, 21, 18]
df['Student'] = [True, True, False, True]

print("--- Initial DataFrame ---")
print(df, "\n")

# Adding Row to DataFrame
new_row = pd.DataFrame([['Sophia', 22, False]], columns=['Name', 'Age', 'Student'])
df = pd.concat([df, new_row], ignore_index=True)

print("--- DataFrame After Adding Row ---")
print(df)