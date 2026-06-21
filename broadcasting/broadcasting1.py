import numpy as np

# Initializing the arrays
arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

# Printing the shapes of arrays
print(arr1.shape)
print(arr2.shape)

# Printing the product of arrays
print(arr1 * arr2)

# Note: Broadcasting fails when array shapes are incompatible: dimensions must either match or be one. Otherwise, NumPy cannot align the data. We have to keep that in mind before coding on numpy.