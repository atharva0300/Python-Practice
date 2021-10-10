import string 

result = string.ascii_letters 
print(result)
a=  input("Enter : ")
for i in range(26): 
    if a==result[i]: 
        print("Letter found")

import random

# generate a random string 
def r(size): 
    result = ''.join([random.choice(string.ascii_letters + string.digits)for n in range(size)])
    return result

get_here = r(10)
print(get_here)

here = ''.join([random.choice(['a' , 'b' , 'c' , 'd']) for n in range(3)])
print(here)

# lower case 
s = input("Enter string : ")
print(s.lower())
print(s.islower())
print(s.isupper())
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())

here = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(3))
print(here)

here = string.digits
print(here)
print(string.ascii_letters)
print(string.hexdigits)
print(string.digits)
s = input("Enter : ")
for i in range(len(s)): 
    if s not in string.hexdigits: 
        print("not here")
    else : 
        print("its there")
        
here  = ''.join(random.choice(string.hexdigits) for n in range(10))
print(here)
here = ''.join(random.choice(string.digits) for n in range(10))
print(here)
