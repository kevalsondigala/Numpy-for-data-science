import numpy as np


# numpy uses 0-based indexing
# numpy also supports -ve indexing

arr = np.array([10, 20, 30 , 40, 50, 60])

# access the elements from the array through indexing
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) # last element


"""
slicing

array[start: stop: step]
arr[start: stop] | start to stop - 1
negative step, -1 reverse

similar type of logic as in python list slicing
"""

print(arr[1:5])
print(arr[::-1])


"""
-------------------
Fancy indexing
-------------------
Fancy indexing in NumPy is an advanced method for selecting multiple, 
non-contiguous elements from an array using an array or list of indices. 
Unlike simple indexing, which accesses single elements or contiguous slices, 
fancy indexing allows for flexible and powerful data extraction and manipulation.

"""

print(arr[[0, 1, -1]])


"""
----------------------
Boolean masking
----------------------
a powerful technique for selecting, extracting, modifying, or counting elements 
within a NumPy array based on specific conditions. It involves creating a "mask" 
array composed of boolean values (True or False), which is then used to index another array.

"""

print(arr[arr > 49 ])

