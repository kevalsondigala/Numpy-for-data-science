import numpy as np

"""
nan - not a number

1. np.isnan() - to detect the missing values
2. np.nan - not a number

"""


# np.isnan()

arr = np.array([1, 2, 3, np.nan, 5, 6, np.nan, np.nan])
print(np.isnan(arr)) # It returns a boolean masking

"""
In the list
True means there is some missing values/np.nan at that position
False means there is not
"""

print(np.nan == np.nan) # This is False
print(np.nan != np.nan) # This is True
"""
This is because 2 unknown/undefined values cannot be equal
"""