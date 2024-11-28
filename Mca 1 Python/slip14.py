# . 1 Write a program which finds sum of digits of a number.           
# Example n=130 then output is 4 (1+3+0). 
n=int(input("Enter no"))
to=0
for i in str(n):
    to=to+int(i)
print(f"the total of {n} is: {to}")

# Input: Tuple and element to search

# tup = tuple(input("Enter elements of the tuple (space-separated): ").split())
# element = input("Enter the element to check: ")

# # Check if the element exists in the tuple
# if element in tup:
#     print(f"{element} is present in the tuple.")
# else:
#     print(f"{element} is not present in the tuple.")


# . 2 Write a Python program to check whether a given element is present in the given 
# tuple. Display the appropriate message. 

tup=tuple(input("Enter values in tuple").split())
el=input("Enter element to check")
if el in tup:
    print(f"{el} is present in tuple")
else:
    print(f"{el} is not present inside a tuple")