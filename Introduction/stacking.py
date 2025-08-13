"""

vertically
horizantally

vstack() -  row wise
hstack() - column wise 

"""


import numpy

arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])
arr3 = numpy.array([4, 5, 6])

print("vertical stack result ->\t", numpy.vstack((arr1, arr2, arr3)), end="\n\n") # vertical stacking


print("horizantal stack result ->\t", numpy.hstack((arr1, arr2, arr3))) # horizantal stacking