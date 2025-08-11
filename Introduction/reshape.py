import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])

# reshaping 1d array to 2d
arr_2d = arr_1d.reshape(1, -1)

print(arr_2d)

# reshaping 2d array to 3d
arr_3d = arr_1d.reshape(2, 3, copy=False)
print(arr_3d)

print(f"3-d array = {arr_3d}")
