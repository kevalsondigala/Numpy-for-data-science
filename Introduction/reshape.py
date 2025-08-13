import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])

# reshaping 1d array to 2d
arr_2d = arr_1d.reshape(1, -1)

print(arr_2d)

# reshaping 2d array to 3d
arr_3d = arr_1d.reshape(2, 3, copy=False)
print(arr_3d)

print(f"3-d array = {arr_3d}")


"""
Flatten the multi-dimensional array in 1-d

np.ravel() -> returns the view/original reference. any modification to ravel changes the original also
np.flatten() -> returns the copy

"""
print("================\n")
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)


flatten = array.flatten()
flatten[0] = 23
print(flatten, array)

ravel = array.ravel()
print(ravel)
ravel[0] = 349273
print(ravel, array)