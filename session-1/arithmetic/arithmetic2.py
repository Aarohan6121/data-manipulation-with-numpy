import numpy as np

# Initializing the arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
scores = np.array([91, 55, 100, 73, 82, 64, 86, 99, 100, 100])

# Element wise arithmetic
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** arr2)

# Comparison operators
# Filtering the failed ones
print(scores < 60)

# Filtering the passed ones
print(scores > 60)

# Filtering the perfect scores
print(scores == 100)