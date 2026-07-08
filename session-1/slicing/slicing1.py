import numpy as np

# Initializing the array
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# Printing alternative columns
print(array[0:4:2])

# Printing last or fourth row
print(array[:, 3])

# Printing the first three columns
print(array[:, 0:3])

# Printing the even nos
print(array[:, 1::2])

# Printing the odd nos
print(array[:, 0::2])