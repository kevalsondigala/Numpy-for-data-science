import numpy as np

"""
Vectorization-
It makes the operations on every single element of the numpy array faster and easier
without using for loops
    
"""

# Without vectorization (pure Python loop)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
result = [x + y for x, y in zip(a, b)]  # slow for large arrays

# With vectorization (NumPy)
arr1 = np.array(a)
arr2 = np.array(b)
result = arr1 + arr2  # fast
print(result)