# Q.1 Write a Python Program to Check if a Number is Positive, Negative or Zero. [10M] 
no=-10
if(no>0):
    print("number is postive")
elif(no<0):
    print("number is negative")
elif(no==0):
    print("number is zero")

# Q.2 Write a program which accepts 6 integer values and prints “DUPLICATES” if any 
# of the values entered are duplicates otherwise it prints “ALL UNIQUE”. 
# Example: Let 6 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be 
# printed
# num=[int(input("Enter number: {}".format(i+1))) for i in range(6)]
# if len(set(num))<len(num):
#     print("DUPLICATES")
# else:
#     print("All unque")

x=[int(input("Enter a list:{}".format(i+1)))for i in range(6)]
if len(set(x))<len(x):
    print("Dublicate")
else:
    print("unique")