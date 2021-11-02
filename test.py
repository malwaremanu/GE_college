import hashlib
  
# initializing string
str2hash = "school1"

# school1 - cbaa409f6e2470985887affe76e0d0ee  
# school2 - 562707810f6c55d8330f1748a206ee2b

#           cbaa409f6e2470985887affe76e0d0ee

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())