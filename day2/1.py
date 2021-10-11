# sets 
s = set()
print(s)

s =set('arhaa')
print(s)

person =  'person'
s = set(person)
print(s)

s = set([1,2,3])
print(s)
s = set((1,2,3))
print(s)
s = set([1,'a' , 2 , 'b' , 3 , 3])
print(s)
s.add(12)
s.add(10)
s.add('person')
print(s)
for i in s: 
    print(i)
print(1 in s)
print('pakoda' in s)

# pop in set () 

s = set([1,2,3,4,5,'person'])
s.pop();
print(s)
s.remove(3)
print(s)
s.clear()
print(s)
# froozen sets 
s = set(['a' , 'b', 'c' ,'d' , 'b' , 'a'])
print(s)
b = frozenset(s)
print(b)

# copy() - returns a shallow copy of the set 
b = s
print(b)
b.pop()
print(b)
print(s)
b= s.copy()
print(b)
b.pop()
print(b)
print(s)
