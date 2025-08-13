import numpy

"""
np.split() -> to split array in equal parts

np.hsplit() -> to split array horizantally

np.vsplit() -> to split array vertically


"""

arr = numpy.array([12, 13, 39, 36, 238, 239])

# Number of splits possible formula = len(arr) / 2,  i.e 1, 2, 3 for length 6 & 1, 2 for length 4 etc.

print(numpy.split(arr, 2), end="\n\n")  # normal split



"""=================== Vertical Split ==============================="""

arr = numpy.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]])

# Split into 2 equal parts vertically
print(numpy.vsplit(arr, 2))


""" =================== horizantal Split =============================== """
print(numpy.hsplit(arr, 3))