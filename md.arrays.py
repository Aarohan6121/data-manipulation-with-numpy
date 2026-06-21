import numpy as np

# 0-dimensional array (Scalar)
array1 = np.array(42)
print(array1.ndim)

# 1-dimensional array (Vector)
array2 = np.array([1, 2, 3])
print(array2.ndim)

# 2-dimensional array
array3 = np.array([['a', 'b', 'c'],
                 ['d', 'e', 'f'],
                 ['g', 'h', 'i']])
print(array3.ndim)

# 3-dimensional array
array4 = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])
print(array4.ndim)

# Multidimensional Indexing 'f'
print(array3[1, 2])

# Multidimensional Indexing 'P'
print(array4[1, 2, 0])

# Writing a word with indexing
word = array4[0, 0, 0] + array4[0, 0, 0] + array4[1, 2, 2] + array4[1, 1, 2] + array4[0, 2, 1] + array4[0, 0, 0] + array4[1, 1, 1]
print(word)