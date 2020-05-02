#############################

import numpy as np

'''
Different types of numpy methods used in this file are :
arange - range of elements - np.arange(0,10)
where - where a condition satisfies - np.where(arr % 2 != 0, -1, arr) - (condition, if true, if false)
full - if we want same value in complete matrix - np.full((3,3), True, dType=bool)
reshape - reshape any array in m & n rows and columns - arr.reshape(2, -1) - giving -1 in column, automatically takes number of columns
vstack - vertically stack two arrays - np.vstack([a, b])
c_ - vertically stack two arrays - np.c_[a,b]
hstack - horizontally stack two arrays - np.hstack([a,b])
r_ - horizontally stack two arrays - np.r_[a,b]
concatenate - combine two arrays - np.concatenate([a,b], axis=0) - axis 0 means row wise combination
intersect1d - find intersection of two arrays - np.intersect1d(a,b)
repeat - repeats the value of array continuously n number of times - np.repeat(arr, 3)
tile - repeats the array continuously n number of times - np.tile(arr, 3)
setdiff1d - arr1 minus(-) arr2 - np.setdiff1d(arr1, arr2)
where - get the index of an element - np.where(a == 2)
vectorize - vectorize any method having int arguments to handle arrays as well - np.vectorize(maxx, otypes=[float])

'''

'''


weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)
'''
#############################
'''
#Write a NumPy program to get the numpy version and show numpy build configuration
print(np.__version__)
print(np.show_config())
'''
############################# Create a 1D array of numbers from 0 to 9
'''
a = np.arange(0, 10)
print(a)
'''
############################# Create a 3×3 numpy array of all True’s

# a = np.array([(True, True, True), (True, True, True), (True, True, True)])

# a = np.full((3,3), True, dtype=bool)

# a = np.ones((3, 3), dtype=bool)

# print(a)

############################# How to extract items that satisfy a given condition from 1D array?

'''
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
cond = arr % 2 != 0
arr1 = arr[cond]
print(arr1)
'''

############################# How to replace items that satisfy a condition with another value in numpy array?

'''
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
cond = arr % 2 != 0
arr[cond] = -1
print(arr)
'''

############################# How to replace items that satisfy a condition without affecting the original array?

# Replace all odd numbers in arr with -1 without changing arr
'''
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)
print(out)
'''
############################# How to reshape an array?

# Convert a 1D array to a 2D array with 2 rows
'''
arr = np.arange(10)
arr1 = arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols
print(arr1)
'''
############################# How to stack two arrays vertically?

# Stack arrays a and b vertically

'''
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

c = np.concatenate([a,b], axis=0)
# c = np.vstack([a,b])
# c = np.r_[a,b]
print(c)
'''

############################# How to stack two arrays horizontally?

# Stack the arrays a and b horizontally.

'''
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# out = np.hstack([a, b])
# out = np.concatenate([a, b], axis=1)
out = np.c_[a,b]
print(out)
'''

############################# How to generate custom sequences in numpy without hardcoding?

# Get the common items between a and b

'''
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

out = np.intersect1d(a, b)
print(out)
'''

#############################  Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
# > array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

'''
a = np.array([1,2,3])
out = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(out)
'''

############################# How to remove from one array those items that exist in another?

#  From array a remove all items present in array b

'''
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

out = np.setdiff1d(a, b)
print(out)
'''

############################# How to get the positions where elements of two arrays match?

# Get the positions where elements of a and b match

'''
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

out = np.where(a == b)
print(out)
'''

############################# How to extract all numbers between a given range from a numpy array?

# Get all items between 5 and 10 from a.

'''
a = np.array([2, 6, 1, 9, 10, 3, 27])

# index = np.where((a >= 5) & (a <= 10))
# index = np.where(np.logical_and(a >= 5, a <= 10))
# print(a[index])
print(a[(a >= 5) & (a <= 10)])
'''

############################# How to make a python function that handles scalars to work on numpy arrays?

# Convert the function maxx that works on two scalars, to work on two arrays.

'''def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))
'''

############################# How to swap two columns or rows in a 2d numpy array?

# Swap columns 1 and 2 in the array arr.

'''
arr = np.arange(9).reshape(3, 3)
print(arr[:,[1,0,2]])

# Swap rows 1 and 2 in the array arr.

arr = np.arange(9).reshape(3, 3)
print(arr[[1,0,2], :])
'''

############################# How to reverse the columns of a 2D array?

# arr = np.arange(9).reshape(3,3)

# print(arr[:, ::-1])

############################# How to reverse the rows of a 2D array?
# print(arr[::-1, :])

