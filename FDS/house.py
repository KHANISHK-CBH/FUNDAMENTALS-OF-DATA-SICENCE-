import numpy as np
house_data = np.array([
    [3, 1400, 7500000],
    [5, 2200, 12500000],
    [4, 1800, 9800000],
    [6, 3000, 18500000],
    [2, 1100, 5200000]
])
mask = house_data[:, 0] > 4
filtered_prices = house_data[mask, 2]
average_price = np.mean(filtered_prices)
print(f"Filtered Prices: {filtered_prices}")
print(f"Average Sale Price: {average_price}")