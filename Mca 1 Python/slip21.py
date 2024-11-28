# Q.1 Write a Python script to access the value of a key from a dictionary


my_dict = {'sr.No 1': 200 , 'sr.No 2':500 , 'sr.No 3': 1000 , 'sr.No 4':10}

# for key, value in my_dict.items():
#     print(f"Key is: {key}, Value is: {value}")

c=list(my_dict.values())
print(c)