# <!-- #The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view. -->

import numpy as np


# VIEW
# -------------------- type your code here ---------------------------------------

# arr = np.array([3,6,8,9])

# x = arr.copy()
# arr[0] = 42
# arr.view()

# print(arr)
# print(x)
 # Make changes in the view 
# -------------------- type your code here ---------------------------------------

# arr = np.array([89,5,657,564])

# x = arr.view()
# arr[0] = 6858

# print(arr)
# print(x)

# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.
# -------------------- type your code here ---------------------------------------
arr = np.array([89,5,657,564])

x = arr.view()
y = arr.copy()

print(y.base)
print(x.base)