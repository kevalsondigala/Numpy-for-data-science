"""
Fill the empyty/missing/nan and inf values
"""
import numpy as np


# np.nan_to_num(arr, nan=<any data>)

arr = np.array([1, 2, 3, np.nan, -np.nan, 6, 7, np.nan])
print(np.isnan(arr))
print(np.nan_to_num(arr, nan=1.1))  


# np.inf(arr)
# To check any infinite values in array

array = np.array([1, 2, np.inf, -np.inf, 73, 63.81, np.inf, np.nan])
print(np.isinf(array))

# To replace infinite values in array

print(np.nan_to_num(array, nan=900, posinf=1000, neginf=-1000)) # replacing both nan and inf values
"""
posinf - replace positive infinity values
neginf - replace negative infinity values
"""
