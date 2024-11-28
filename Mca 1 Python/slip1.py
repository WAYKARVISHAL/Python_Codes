# Q. 1 Write a Python program to calculate the average of numbers in a given list.
num=[1,2,3,5,6]
ave=sum(num)/len(num)
print("the average is :",ave)


# Q. 2 Write an anonymous function to display the cube of all elements in the list.
# no=[1,3,5,6,8]
# cube=list(map(lambda x:x**3,no))
# print("cube the elements:",cube)

num=[1,3,4,5]
cube=list(map(lambda x:x**3,num))
print("cube of the no is:=",cube)