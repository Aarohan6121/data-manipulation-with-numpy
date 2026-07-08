import numpy as np

# Initializing the array
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# Printing the columns in reversed
print(array[:, ::-1])

# Printing 1st Quadrant
print(array[0:2, 2:])

# Printing 2nd Quadrant
print(array[0:2, 0:2])

# Printing 3rd Quadrant
print(array[2:, 0:2])

# Printing 4th Quadrant
print(array[2:, 2:])