import numpy as np
from scipy import stats
from scipy.stats import norm, pearsonr
from scipy import linalg
from scipy.optimize import minimize

print("--- SciPy Central Tendency Examples ---")
data = [10, 20, 30, 40, 50]
print("Mean:", np.mean(data))
print("Median:", np.median(data))
mode_result = stats.mode(data, keepdims=True)
print("Mode:", mode_result.mode[0], "Count:", mode_result.count[0], "\n")

print("--- Probability Distribution Example ---")
probability = norm.cdf(85, loc=70, scale=10)
print("Probability:", probability, "\n")

print("--- Hypothesis Testing Example ---")
data2 = [22, 25, 19, 24, 28, 30]
t_stat, p_value = stats.ttest_1samp(data2, 25)
print("T-Statistic:", t_stat)
print("P-Value:", p_value, "\n")

print("--- Correlation Example ---")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
corr, p_value_corr = pearsonr(x, y)
print("Correlation:", corr, "P-Value:", p_value_corr, "\n")

print("--- Linear Algebra Example ---")
A = np.array([[3, 2], [1, 2]])
B = np.array([5, 5])
solution = linalg.solve(A, B)
print("Linear system solution:", solution, "\n")

print("--- Optimization Example ---")
def objective(x):
    return x[0]**2 + 4

result = minimize(objective, x0=[5])
print("Optimization result x:", result.x)
print("Optimization success:", result.success)
