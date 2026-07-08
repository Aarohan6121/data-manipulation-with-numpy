import numpy as np

# Initializing the array
array = np.array([1, 2, 3, 4, 5])
random = np.random.default_rng()

# Shuffles the array in a random order
random.shuffle(array)

# 3 dimensional space of random array nos
casino_array = random.choice(array, size=(3, 3))

# Printing the outputs
print(array)
print(casino_array)