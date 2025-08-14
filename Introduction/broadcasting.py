import numpy as np


""" problem without broadcasting"""


prices = [100, 200, 300]

discount = 10 # in %

final_prices = []

for price in prices:
    final_price = price - (price * discount / 100)
    # print(price * discount / 100)
    # print(final_price)
    final_prices.append(final_price)


# print(final_prices)

"""

so for very large data set it will be very time consuming to perform 
expensive operations

So here broadcasting come into picture
- loops will be cut-off
- faster and easier

Rules*
1. matching shape/dimension
2. expanding single elements
3. incompatible shapes, it will throw error

"""

""" Using broadcasting """

prices = np.array(np.arange(100, 1001, 100))
discount = 10

final_prices = prices - (prices * discount / 100)

print(final_prices)

# single element broadcasting

arr = np.array([100, 200, 300])
print(arr * 2)

# 2-d matrix broadcasting

matx = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

print(matx + vector) 
""" Output:-
[
    [11 22 33]
    [14 25 36]
]
"""


# numpy will automatically make the arrays complatible for the different shape and dimensions arrays
arr1 = np.array([[1], [2], [3]])
arr2 = np.array([1, 2])
# print(arr1.ndim, arr2.ndim)
print(arr1 + arr2)