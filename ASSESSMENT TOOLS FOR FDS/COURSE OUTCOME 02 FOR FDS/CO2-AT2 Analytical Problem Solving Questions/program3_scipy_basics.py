import numpy as np
from scipy import stats, linalg
from scipy.stats import norm, pearsonr
from scipy.optimize import minimize

# 1. Measures of Central Tendency
data = [10, 20, 30, 40, 50]
print("--- Central Tendency ---")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))

# 2. Probability Distribution Analysis
probability = norm.cdf(85, loc=70, scale=10)
print("\n--- Probability Distribution ---")
print("Probability:", probability)

# 3. Hypothesis Testing (1-sample t-test)
test_data = [22, 25, 19, 24, 28, 30]
t_stat, p_val_ttest = stats.ttest_1samp(test_data, 25)
print("\n--- Hypothesis Testing ---")
print("T-Statistic:", t_stat)
print("P-Value:", p_val_ttest)

# 4. Correlation Analysis
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
corr, p_val_corr = pearsonr(x, y)
print("\n--- Correlation Analysis ---")
print("Correlation:", corr)

# 5. Linear Algebra Operations
A = [[3, 2], [1, 2]]
B = [5, 5]
solution = linalg.solve(A, B)
print("\n--- Linear Algebra ---")
print("Solution:", solution)

# 6. Optimization
def objective(x):
    return x**2 + 4

result = minimize(objective, x0=5)
print("\n--- Optimization ---")
print("Optimal x:", result.x)