# # .1 Write a Python program to count the number of occurrences of each 
# character in a string. Sample String: google.com' 
# Expected Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 
# def count(strr):
#     ch={}
#     for i in strr:
#         if i in ch:
#             ch[i]+=1
#         else:
#             ch[i]=1
#     return ch

# strr="vishalvijaywaykar"
# result=count(strr)
# print(result)

def coun(n):
    ch={}
    for i in n:
        if i in ch:
            ch[i]+=1
        else:
            ch[i]=1
    return ch


stri="Google"
res=coun(stri)
print(res)



