import numpy as np
X = np.array([
    [1, 3, 120],
    [6, 15, 300],
    [0, 1, 80],
    [4, 10, 250],
    [2, 5, 160]
])

X_bias = np.c_[np.ones(X.shape[0]), X]
y = np.array([0, 1, 0, 1, 0])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
weights = np.zeros(X_bias.shape[1])
learning_rate = 0.0001
for _ in range(5000):
    predictions = sigmoid(np.dot(X_bias, weights))
    errors = predictions - y
    gradient = np.dot(X_bias.T, errors) / len(y)
    weights -= learning_rate * gradient  # Update weights
print("Model Trained ")
new_email = np.array([1, 5, 12, 270])  # Note the 1 at the beginning for the bias
probability = sigmoid(np.dot(new_email, weights))

print(f"Spam Probability: {probability:.2%}")
if probability >= 0.5:
    print("Result: SPAM (1)")
else:
    print("Result: NOT SPAM (0)")