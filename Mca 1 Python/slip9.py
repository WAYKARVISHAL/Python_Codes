# Q. 1. Write a Python program to calculate the average of numbers in a given list. 
li=[1,2,4,5]
re=sum(li)/len(li)
print(re)


# Q. 2. Create a function showEmployee(), pass employee name and salary as parameters 
# and display both, and if the salary is missing in function call it should show that 
# # it is Rs. 90000.

def showEmployee(name,salary=90000):
    print(f"Employee name{name}, Salary is .{salary}")

showEmployee("vishal",salary=3000)
showEmployee("taki")

