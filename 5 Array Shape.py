import numpy as np 

arr = np.array([[1,2,34,56], [5,6,3,2,]])
print(arr.shape)


# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1,2,3,4,5], ndmin = 5 )

print(arr)
print("Shape of array is : ", arr.shape)
