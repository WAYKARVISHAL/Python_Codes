# .1 Write a Python Program to Find the Factorial of a Number. 
# def Factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*Factorial(n-1)
# no=int(input("Enter no"))
# print(f"the factorial of{no} is {Factorial(no)}")

# Q2. Create two classes : Person class having attributes name, age and Company class 
# having attributes cname, location. The class Employee will inherited from both 
# classes having attributes salary, skill. Display all information of the employee

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Company:
    def __init__(self,cname,location):
        self.cname=cname
        self.location=location
class Employee(Person,Company):
    def __init__(self,name,age,cname,location,salary,skill):
        Person.__init__(self,name,age)
        Company.__init__(self,cname,location)
        self.salary=salary
        self.skill=skill
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("cname",self.cname)
        print("location",self.location)
        print("salary",self.salary)
        print("skill",self.skill)
emp=Employee(name="vishal",age="20",cname="nope",location="pune",salary="100",skill="wt")
emp.display()