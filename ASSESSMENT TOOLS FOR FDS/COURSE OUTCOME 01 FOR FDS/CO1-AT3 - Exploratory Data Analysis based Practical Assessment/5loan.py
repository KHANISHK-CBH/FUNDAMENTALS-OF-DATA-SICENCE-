import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
data = {
    'Applicant_ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'Income': [45000, 30000, 60000, 28000, 52000],
    'Credit_Score': [720, 650, 780, 620, 710],
    'Existing_Loans': [0, 1, 0, 2, 1],
    'Approved': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
X = df[['Income', 'Credit_Score', 'Existing_Loans']]
y = df['Approved']
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X, y)
print("--- Question 5: CART Decision Tree Model Trained ---\n")
print("--- Generated Decision Tree Rules ---")
tree_rules = export_text(clf, feature_names=['Income', 'Credit_Score', 'Existing_Loans'])
print(tree_rules)
print("-------------------------------------\n")
new_applicant = pd.DataFrame([[40000, 700, 1]], columns=['Income', 'Credit_Score', 'Existing_Loans'])
loan_prediction = clf.predict(new_applicant)
result = "Approved" if loan_prediction[0] == 1 else "Rejected"
print(f"Prediction for Test Applicant: {result}")