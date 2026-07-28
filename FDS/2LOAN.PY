import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    'Email_ID': ['E1', 'E2', 'E3', 'E4', 'E5'],
    'Num_Links': [1, 6, 0, 4, 2],
    'Num_Caps_Words': [3, 15, 1, 10, 5],
    'Email_Length': [120, 300, 80, 250, 160],
    'Spam': [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X = df[['Num_Links', 'Num_Caps_Words', 'Email_Length']]
y = df['Spam']
model = LogisticRegression()
model.fit(X, y)

print("--- Model Training Complete ---")
print(f"Intercept (w0): {model.intercept_[0]:.4f}")
print(f"Coefficients (w1, w2, w3): {model.coef_[0]}\n")

new_email = np.array([[3, 7, 180]])
prediction = model.predict(new_email)
probability = model.predict_proba(new_email)

status = "Spam" if prediction[0] == 1 else "Not Spam"

print("--- Prediction for New Email ---")
print(f"Features entered -> Links: 3, Caps Words: 7, Length: 180")
print(f"Result: The email is classified as **{status}**")
print(f"Probability breakdown -> Not Spam: {probability[0][0]:.2%}, Spam: {probability[0][1]:.2%}")