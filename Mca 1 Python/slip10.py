# Q.1 Write a Python function to find the Max of three numbers.         
a=10
b=22
c=33
if(a>b and a>c):
    print(f"{a} is max")
elif(b>c and b>a):
    print(f"{b} is max")
else:
    print(f"{c}is max")


# Q.2 Write a Python program to remove duplicate elements from the list.  
li=[1,2,3,4,3,2]
print(li)
print("After removing:")
l1=set(list(li))
print(l1)