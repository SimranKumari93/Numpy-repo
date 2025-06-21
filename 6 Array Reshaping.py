import numpy as np 

# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.


# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr1 = arr1.reshape(4, 3)  
# print(newarr1)

# Reshape From 1-D to 3-D
# -------------------- type your code here ---------------------------------------

# arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr2 = arr2.reshape(2, 3, 2)  
# print(newarr2)


# Returns Copy or View?
# -------------------- type your code here ---------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)
# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# -------------------- type your code here ---------------------------------------

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr3 = arr3.reshape(2, 2, -1)  
print(newarr3)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
# -------------------- type your code here ---------------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)