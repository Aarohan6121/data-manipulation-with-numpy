import numpy as np

# Initializing the array
array = np.array([1.1, 2.2, 3.3])

# Scalar Arithmetic
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# Vector Arithmetic
# Accessing square root of the nos
print(f"\n{np.sqrt(array)}")

# Round up : ceil() func
print(np.ceil(array))

# Round down : floor() func
print(np.floor(array))