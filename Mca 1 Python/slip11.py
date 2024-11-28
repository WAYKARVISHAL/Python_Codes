# Q.1 Write a Python function that takes a number as a parameter and display factorial 
# of it. 
# def fact(n):
#     if n==0:
#         print(f"the fact {n} is not ")
#     elif n==0 or n==1:
#         print(f"the factor {n} is 1")
#     else:
#         fact =1
#         for i in range(1,n+1):
#             fact *=i
#         print(f"the {n} is {fact}")
# num=int(input("Enter no"))
# fact(num)


# Q.2 Write a NumPy program to get the unique elements of an array. 
import numpy as np
l=np.arr([1,3,4,5])
uni=np.unique(l)
print(uni)