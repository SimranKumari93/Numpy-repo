import numpy as np 

# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
# Split the array in 3 parts:
# -------------------- type your code here --------------------------------------- 

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr) 

# Split Into Arrays
# The return value of the array_split() method is an array containing each of the split as an array.
# If you split an array into 3 arrays, you can access them from the result just like any array element:
# -------------------- type your code here ---------------------------------------

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.
# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
# -------------------- type your code here ---------------------------------------

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

# Split the 2-D array into three 2-D arrays along columns.
# -------------------- type your code here ---------------------------------------

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# An alternate solution is using hsplit() opposite of hstack()
# -------------------- type your code here ---------------------------------------

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)