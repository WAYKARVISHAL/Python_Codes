# . 1 Write a recursive function to calculate the sum of numbers from 0 to n. 

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + recursive_sum(n-1)
# num=int(input("Enter a number"))
# print("the sum of number 0 to ",num,"is",recursive_sum(num))
# def recuresive_sum(n):
#     if n==0:
#         return 0
#     else:
#         return n +recuresive_sum(n-1)
# n=int(input("Enter no"))
# print(f"the sum of {n} is: {recuresive_sum(n)}")

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# no=int(input("enter number:"))
# result=sum(no)
# print("the sum of number 0 to",no,"is",result)

# Q. 2 Write a lambda expression to replace characters of given string by other character.

# replace_char = lambda s, old, new: s.replace(old, new)
# input_str=input("Enter string:")
# old=input("Enter character replace:")
# new=input("Enter character:")
# result=replace_char(input_str,old,new)
# print("modified string is:",result)

modifie=lambda s,old,new:s.replace(old,new)
n=input("Enter string:")
old=input("Enter character replace:")
new=input("Enter char to change:")
print(f"modified string is ",modifie(n,old,new))
