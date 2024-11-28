# .1 Write a Python program to print list after removing ODD numbers. 

# num=[1,2,3,4,5]
# print("Original list: ",num)
# n1=[]
# for i in num:
#     if i%2==0:
#         n1.append(i)
# print(n1)

    # Q.2 Create two classes : Person class having attributes name, age and Company class 
    # having attributes cname , location. The class Employee will inherited from both 
    # classes having attributes salary, skill. Display all information of the employee.

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

emp=Employee(name="vishal",age="age",cname="cname",location="pune" ,salary="10000",skill="python")
emp.display()