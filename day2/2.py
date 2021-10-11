# collectios module

from collections import Counter 
import string 

print(Counter([1,2,3,4,1,2,3,6,7,5,6,7,]))
print(Counter(['a' , 't' , 'h'  ,'a' , 'r' , 'v', 'a']))
print(Counter([string.ascii_letters]))
print(Counter(a = 3 , b=1 , c = 4))
# order dict in python 

from collections import OrderedDict 
d = {} 
d[1] =1
d[2] = 2
d[3] = 3
d[4]= 4
print(d)
for key, item in d.items(): 
    print(key , ": " , item)
print(len(d))

d.pop(2)
print(d)
d[2] = 1
print(d)
d.pop(2)
print(d)

# defauult dict 

from collections import defaultdict 

d = {} 
d =defaultdict(int)
print(d)

l = [1,5,7,3,5,7,9]
for i in l: 
    d[i] = d[i]+1

print(d)

d = defaultdict(list)
for i in range(5): 
    d[i].append(i)

print(d)

# chainmap 

from collections import ChainMap

d1 = {'a': 1 , 't' : 2}
d2 = {'h' : 3 , 'a' : 5}
c = ChainMap(d1, d2)
print(c)

for i in c.items() :
    print(i)

print()
for key , item in c.items() :
    print(key , ': ' , item)

print(c.keys())
print(c.items())
print(c.values())

# Named tuple 

from collections import namedtuple 

student = namedtuple('Student' , ['name' , 'age' , 'DOB'])
print(student)

s =student('atharva' , '1' , '2')
print(s)

a = namedtuple('atharva' ,['gender' , 'age' , 'phone_number'])
b = a('male' , '20', 123459580943)
print(b)
print(b.gender)
print(b.age)
print(b.phone_number)


li = [1,2,3]
s = namedtuple('person' , ['one' ,'two' , 'three'])
print(s._make(li))
person  = s('one_number' , 'two_number' ,'three_number')
print(person._asdict())

# deque 

from collections import deque

d = deque(['name' , 'age' , 'number'])
print(d)

de = deque([1,2,3])
de.append(123)
print(de)
de.pop()
print(de)
de.appendleft(12)
print(de)
de.pop()
print(de)



