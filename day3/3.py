# chainmap in python

from collections import defaultdict 
from collections import ChainMap

d = defaultdict()
d[1] = 'person'
d[2] = 'atharva'
e = {}
e[1] = 123
e[3] = 234
a = ChainMap(d,e)
print(a)
for key, values in a.items(): 
    print(key , " : " , values)

print(list(a.keys()))
print(list(a.values()))
print(a.maps)
b = {} 
b[1] = 324
b[2] = 456
a = a.new_child(b)
print(a)

# using reverse 
a.maps = reversed(a.maps)
print(a)

# named tuple 
from collections import namedtuple 

s = namedtuple('person' , ['name' , 'age' ,'person1'])
temp = s('atharva' , 12  , 1234)
print(temp)
print(temp.name)
print(temp.age)
print(temp[1])
print(getattr(temp , 'name'))
print(getattr(temp , 'person1'))

# Conversion operations 
print(temp._asdict())
l = ['aditya' , 34 , 45]
print(s._make(l))

from collections import defaultdict

def value(): 
    return "Not present"
d = defaultdict(lambda : value)
d['name'] = 'pingale'
d['age'] =23
d['person1'] = 56
print(d)

print(s(**d))

# Additional Operations 
print(s._fields)
# display all the fieds of the 's' namedtuple 
