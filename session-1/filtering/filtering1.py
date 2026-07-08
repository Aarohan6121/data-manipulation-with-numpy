import numpy as np

# Initializing the array
ages = np.array([[21, 17, 20, 16, 30, 18, 19], 
                 [39, 34, 15, 32, 38, 31, 23]])

teenagers = ages[ages < 18]
early_adults = ages[(ages >= 18) & (ages < 25)]
mid_adults = ages[(ages >= 25) & (ages < 35)]

print(teenagers)
print(early_adults)
print(mid_adults)