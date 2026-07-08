import numpy as np

# Initializing the array
ages = np.array([[21, 17, 20, 16, 30, 18, 19], 
                 [39, 34, 15, 32, 38, 31, 23]])

late_adults = ages[(ages >= 35) & (ages < 45)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(late_adults)
print(evens)
print(odds)