import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr, end="\n\n")

# or

normal = [1, 2, 3,]
arr = np.array(normal)
print(arr, end="\n\n")

# create with default values with 0's

zeros_arr = np.zeros((3, 2), dtype=dict)
zeros_arr[0] = {}
print(zeros_arr, end="\n\n")

# create with default values with 0's

ones_arr = np.ones((2, 3), dtype=str)
print(ones_arr, end="\n\n")

# create with default values with any data and shape

full_arr = np.full((2, 2), fill_value='k')
print(full_arr, end="\n\n")


# create sequences of numbers in numpy array
# its like a normal range func in python, just a numpy array
# start, stop, step
arr = np.arange(10)
print(arr)
arr = np.arange(1, 10)
print(arr)
arr = np.arange(1, 12, 2)
print(arr, end="\n\n")

# np.eye()
# function is used to create a 2-D array (matrix) where the elements along a specified diagonal are ones, and all other elements are zeros.
# identity matrix

eye_matrix = np.eye(5)
print(eye_matrix)