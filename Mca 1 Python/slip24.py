# Q.1 Write a NumPy program to get the unique elements of an array.


import numpy as np

arr = np.array([1, 2, 3, 4, 2, 99 , 70 , 80])

unique_elements = np.unique(arr)

print("Orignal Array" , arr)
print("Unique Elements in Numpy Array" , unique_elements)


# Q. 2 Write a recursive function to calculate the sum of numbers from 0 to n.

# Recursive function to calculate the sum of numbers from 0 to n
def sum_recursive(n):
    if n < 0:
        return "Please enter a non-negative integer."
    if n == 0:  
        return 0
    return n + sum_recursive(n - 1)


n = int(input("Enter a non-negative integer: "))
result = sum_recursive(n)
print(f"The sum of numbers from 0 to {n} is: {result}")