import numpy as np


arr = np.array([1, 2, 3])
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

"""

insert data
np.insert(array, obj, value, axis=None)
array - original array
obj - The index or indices before which values are inserted. 
        This can be an integer or an array of integers.

values - The values to be inserted. 
        These should be shaped appropriately to be inserted into arr at the specified obj.

axis -
    (Optional) The axis along which to insert the values.
    If axis=0, values are inserted as rows.
    If axis=1, values are inserted as columns.
    If axis=None (default), the array is flattened before insertion, and obj refers to indices in the flattened array.

"""

arr = np.insert(arr_2d, 2, [9, 8], axis=None)
print(arr)


"""     Append       """

a = np.append(arr_2d, [[66, 77]], axis=0)
print(a)


"""  Concatinate  """

# arr1 = np.array([[1, 2, 3, "Hey"]])
# arr2 = np.array([[4, 5, 6]])

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1.shape, arr2.shape)


result = np.concatenate((arr1, arr2), axis=0)
print(result, end="\n\n")
print(result.shape)


""" delete elememts  """
"""

np.delete(array, index, axis=None)

"""

# delete from 1-d array
arr = np.array([1, 23, 22, 54, 45, 77, 12])
new_arr = np.delete(arr, 3)
print(arr, "\t", new_arr)

# delete from 2-d array - row deletion
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr2d = np.delete(arr2d, 0, axis=0)
# print(arr2d, "\t", new_arr2d)

print("=====")
# delete from 2-d array - coluumn deletion
new_arr2d = np.delete(arr2d, (1, 0), axis=1)
print(arr2d, "\t", new_arr2d)