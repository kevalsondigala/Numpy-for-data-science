import numpy as np

# shape of the numpy array
nums = [[1, 2, 3], [4, 5, 6]]
arr = np.array(nums)
print(arr.shape) # (2, 3) rows and columns


# size
# total number of elements
print(arr.size)


# ndim
# no. of dimensions
print(arr.ndim) # 2


print(arr.dtype) # to check type of values in array

new_arr = arr.astype(str)

print(new_arr.dtype)