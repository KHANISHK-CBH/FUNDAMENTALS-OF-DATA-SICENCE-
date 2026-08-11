import pandas as pd
import matplotlib.pyplot as plt

# Load Kaggle Student Performance dataset
df = pd.read_csv('StudentsPerformance.csv')

def assign_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

df['Grade'] = df['math score'].apply(assign_grade)
grade_counts = df['Grade'].value_counts().sort_index()

print("=" * 40)
print("     PROBLEM 2: GRADE FREQUENCY")
print("=" * 40)
print("\nFrequency Distribution Table:")
print(grade_counts)

# Plot Bar Chart
plt.figure(figsize=(8, 5))
grade_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Frequency Distribution of Students' Grades")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()