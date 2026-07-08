import numpy as np

# Initializing the array
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# Aggregate functions (2)
# Standard deviation of the array
print(np.std(array))

# Index of the minimum value
print(np.argmin(array))

# Index of the maximum value
print(np.argmax(array))

# Sum of all the columns
print(np.sum(array, axis=0))

# Sum of all the rows
print(np.sum(array, axis=1))