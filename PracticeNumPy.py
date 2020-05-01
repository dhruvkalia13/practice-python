#############################

import numpy as np

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

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# c = np.concatenate([a,b], axis=0)
# c = np.vstack([a,b])
c = np.r_[a,b]
print(c)
