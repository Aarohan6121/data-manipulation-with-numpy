import numpy as np

random = np.random.default_rng()

# Gives a random int array between 1-100
print(random.integers(low=1, high=101, size=(3, 3)))

# Gives a random float array between 1-10
print(np.random.uniform(low=1, high=10, size=(3, 3)))