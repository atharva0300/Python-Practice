# deque 
from collections import deque

q = deque(['name' , 'age' ,'number'])
print(q)

q.append(4)
print(q)
q.appendleft(12)
print(q)

q.pop()
print(q)
q.popleft()
print(q)

de =deque([1,2,3,3,4,2,4])
print(de.index(4,2,5))
de.insert(4,3)
print(de)
print(de.count(3))
de.remove(3)
print(de)

de.extend([9])
print(de)
de.extendleft([9,9])
print(de)
de.reverse()
print(de)
de.rotate()
print(de)
de.rotate(-1)   # if rotate(negative number) -> then, teh rotation takes place on the left side ,
# else it takes on the right side 
print(de)

# collections userdict in python

from collections import UserDict 

d = {'a' : 1,
     'b' : 2,
     'c' : 3}

user = UserDict(d)
print(user)
print(user.data)
user = UserDict()
print(user)

"""
class MyDict(UserDict): 
    def __del__(self): 
        raise RuntimeError("Deletion not allowed")
    
    def pop(self, s = None ): 
        raise RuntimeError("Deletion not allowed")
    
    def popitem(self, s = None ): 
        raise RuntimeError("Deletion ot allowed")


# Driver Code 
user = MyDict({'a' : 1,
               'b' : 2,
               'c' : 3})

#print(user)
user.pop(1)
"""

# userlist 
from collections import UserList

l = [1,2,3,4]
user = UserList(l)
print(user.data)

userl = UserList()
print(userl.data)

from collections import UserList

class MyList(UserList): 
    def remove(self, s = None): 
        raise RuntimeError("Deletion not allowed ")
    
    def pop(self , s = None): 
        raise RuntimeError("Deletion not allowed")

l = MyList([1,2,3,4])
print(l)
l.append(5)
print(l)
#l.remove()

# Collections.UserString 

from collections import UserString 
d = 12345
s = UserString(d)
print(s.data)

s = UserString(" ")
print(s)

class MyString(UserString): 
    def append(self, s ): 
        self.data= self.data + s
    
    def remove(self , s): 
        self.data = self.data.replace(s , "")

p = MyString("Atharva")
print(p.data)
p.append("s")
print(p)
p.remove("as")
print(p)
p.remove("a")
print(p)
# There's no 'a' in the string here 
# but removing the character 'a'
# won't give an error 
p.remove("a")
print(p)


