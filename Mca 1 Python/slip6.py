# Q.1 Write a Python program to find the Factorial of a Number. 
def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)

no=int(input("Enter no"))
print(f"the factorial {no} is:{Factorial(no)}")
# 
# 2. Write a Python class BankAccount with attributes like account_number, balance, 
# date_of_opening and customer_name, and methods like deposit, withdraw, and 
# check_balance. 

# class BankAccount:
#     def __init__(self,account_number,balance,date_of_opening,customer_name):
#         self.account_number=account_number
#         self.balance=balance
#         self.date_of_opening=date_of_opening
#         self.customer_name=customer_name
#     def deposit(self,amount):
#         if amount>0:
#             self.balance<=self.balance
#             print(f"Deposited {amount} into your account. Your current balance is {self.balance}")
#         else:
#           print("Invalid amount")
        
# def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Successfully withdrew {amount}. Remaining balance is: {self.balance}")
#             else:
#                 print("Insufficient funds!")
#         else:
#             print("Invalid withdrawal amount. Please enter a positive value.")

#     # Method to check the balance
# def check_balance(self):
#         print(f"Account {self.account_number} balance: {self.balance}")

# # Example usage
# account = BankAccount(account_number="987654", customer_name="John Doe", date_of_opening="2024-01-01", balance=5000)

# # Deposit money
# account.deposit(1000)

# # Withdraw money
# account.withdraw(2000)
