import numpy as np

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# -------------------- type your code here ---------------------------------------

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Creating the Filter Array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
# Create a filter array that will return only values higher than 42:
# -------------------- type your code here ---------------------------------------

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
# -------------------- type your code here ---------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating Filter Directly From Array
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
# Example
# Create a filter array that will return only values higher than 42:
# -------------------- type your code here ---------------------------------------

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
# -------------------- type your code here ---------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# d = {'A': 'python', 'B': 'Java'}

# #getting items 
# items = d.items()

# d['C'] = 'C++'

# print(items)

d = {'A': 'python', 'C': 'kubernets', 'B': 'Jira'}

myd = list(d.keys()) # convert dict into list
myd.sort()

sd = {i: d[i] for i in myd} # sorted dictionary 
print(sd)