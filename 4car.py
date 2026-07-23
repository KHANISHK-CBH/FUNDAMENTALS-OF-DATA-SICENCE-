import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    'Car_ID': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'Age': [2, 5, 3, 7, 1],
    'Kms_Driven': [25000, 60000, 40000, 90000, 15000],
    'Engine_CC': [1200, 1500, 1300, 1800, 1000],
    'Resale_Price': [650000, 420000, 520000, 300000, 720000]
}
df = pd.DataFrame(data)
X = df[['Age', 'Kms_Driven', 'Engine_CC']]
y = df['Resale_Price']
car_model = LinearRegression()
car_model.fit(X, y)

print("--- Question 4: Car Price Prediction Model Trained ---\n")
print("Please enter the details for the new car evaluation:")
try:
    user_age = float(input("Enter Car Age (in years): "))
    user_kms = float(input("Enter Total Kilometers Driven: "))
    user_cc = float(input("Enter Engine Capacity (in cc): "))
    user_features = np.array([[user_age, user_kms, user_cc]])
    predicted_price = car_model.predict(user_features)

    print("\n--- Valuation Result ---")
    print(f"Estimated Resale Price: ₹{predicted_price[0]:,.2f}")
except ValueError:
    print("\n[Error] Please enter valid numerical values for the inputs.")