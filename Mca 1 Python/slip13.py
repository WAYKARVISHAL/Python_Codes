
# Q. 1 Write a python program to check if a string is a Palindrome or Not.  
# def palindrome(s):
#     return s == s[::-1]
# s = "madam"
# result = palindrome(s)
# if result:
#     print("yes")
# else:
#     print("No")


def palindrome(s):
    return s==s[::-1]
stri="masdam"
result=palindrome(stri)
if result:
    print(f"the {stri} is palindrome")
else:
    print(f"The {stri} is not palindrome")