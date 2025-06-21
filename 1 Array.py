import numpy as np

# arr = numpy.array((1, 2, 3, 4, 5))  # this is a tuple 
# arr = numpy.array([1, 2, 3, 4, 5])    ## this is an array 

# arr = np.arr(42)
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
# arr = np.array([1,2,3,4,5])

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.

# These are often used to represent matrix or 2nd order tensors.
# arr = numpy.array([[1,2,3], [4,5,6]])
# arr = numpy.array([[1, 2, 3], [4, 5, 6]])

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)

# print(type(arr))

# Higher Dimensional Arrays
# arr = np.array([1, 2, 3, 4], ndmin = 5)

# print(arr)
# print('Number of dimensions: ', arr.ndmin)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)