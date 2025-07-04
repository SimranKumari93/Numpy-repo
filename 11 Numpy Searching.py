import numpy as np 

# Sorting Arrays
# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

#  Sort an array 
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Sort a boolean 
arr = np.array([True, False, True])

print(np.sort(arr))

# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
