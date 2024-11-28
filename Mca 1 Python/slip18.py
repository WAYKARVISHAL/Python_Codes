# Q. 2 Write a NumPy program to test whether every element of an 1-D array is
# present in another array. 


import numpy as np

def is_subset(array1 , array2):
    return np.isin(array1 ,array2).all()

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5,8 , 9 , 10])
result = is_subset(array1 , array2)

print(result)