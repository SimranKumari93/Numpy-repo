import numpy as np 
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([3,6,7,9])
# arr2 = np.array([2,4,6,8])

# newarray = np.concatenate((arr1 , arr2))

# print(newarray)
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed 
# it is taken as 0.
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))
# print(arr)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
# -------------------- type your code here ---------------------------------------

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))
# print(arr)

# Stacking Along Depth
# NumPy provides a helper function: dstack()  to stack along heights(depth).
# -------------------- type your code here ---------------------------------------

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
print(arr)
