# Q.1 Write a Python program to sum all the items in a dictionary.         
# Sample Dictionary: my_dict = {'data1':100,'data2':20,'data3':50} 
# Expected Result: 170

my_dict={'data1':100,'data2':33,'data3':55}
result=sum(my_dict.values())
print(result)



# Q. 2. Write a Python function that takes a number as a parameter and display factorial 
# of it.
# def fact(num):
#     if num<0:
#         print("fibo is not define ")
#     elif num==0 or num==1:
#         print("factorial {num} is 1")
#     else:
#         fact =1
#         for i in range(1,num+1):
#             fact*=i
#         print(f"the factorial of {num} is:{fact}")
# num=int(input("Enter val:"))
# fact(num)

def Factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * Factorial(num-1)
nu=int(input("Enter no"))
print(f"facotrial of {nu} is:{Factorial(nu)}")