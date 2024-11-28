# Q. 1 Create a function showEmployee(), pass employee name and salary as parameters
# and display both, and if the salary is missing in function call it should show that it
# is Rs. 50000 

def showEmpolyee(EName , salary=90000):
    print("Employee Name: ", EName)
    print("Employee Salary :" , salary)


showEmpolyee("vaibav")

# 2 Write a Python program to calculate the average of numbers in a given List. 
ls=[1,2,3,4]
c=sum(ls)/len(ls)
print(c)