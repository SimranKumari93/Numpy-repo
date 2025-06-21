import numpy as np


# simple numpy array 
arr = np.array([1, 2, 3, 4])

# Creating Arrays With a Defined Data Type 
# We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define 
# the expected data type of the array elements:
 # -------------------type your code here ------------------------------------
# arr = np.array([1, 2, 3, 4], dtype = "S") 
# arr = np.array([1, 2, 3, 4], dtype = "i4")

# print(arr)
# print(arr.dtype) 

# ---------------------- Converting Data Type on Existing Arrays -------------------------------------

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type 
# directly like float for float and int for integer.

# change data type from float to integer 
# -------------------- type your code here ---------------------------------------
# arr = np.array([3.8, 4.9, 8.0, 9.6])
# newarray = arr.astype('i')

# print(arr)
# print(newarray.dtype) 

# change data type from integer to boolean 

# -------------------- type your code here ---------------------------------------
arr = np.array([1, 0, 2, 1])

newarray = arr.astype(bool)
print(newarray.dtype)
