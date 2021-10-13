# python collections 

from collections import Counter 

a = [1,2,3,1,2]
print(Counter(a))
print(Counter({'a' :  2 , 'b' : 1 , 'c' : 3}))
print(Counter(A =3 , B=2))
coun  = Counter()
coun.update([1,2,3,2,3,4])
print(coun)
a =['atharva' , 'pingale' , 'atharva' , 'pingale' , 'person']
print(Counter(a))

# ordered dict () 
from collections import OrderedDict
a = {} 
a[1] = 'a'
a[2] = 'b'
a[3] = 'c'
a[4] = 'd'
print(a)
a[3] = 'person'
print(a)
a.pop(2)
print(a)
a[4] = 'person'
print(a)

b = OrderedDict()
b[2] = 'a'
b[1] = '3'
b[4] = 'b'
b[3] ='e'
print(b)
b[4] = 'person'
print(b)
b.pop(3)
b[3] = 'e'
print(b)

# defualt dict ()
d = {1 : 'persoin' , 2: 'atharva' , 3 : 'pingale'}
print(d)
print(d[1])

from collections import defaultdict 


def value() :
    return "Not present"
d = defaultdict(value)
d[1]=  'person'
d[2] = 'atharva'
print(d[1])
print(d[3])

# another way to do this, using hte lambda function
d = defaultdict(lambda : "Not present")
d[1] = 'pingale'
d[2]= 'atharva'
print(d[1])
print(d[3])

print(d.__missing__('atharva'))
print(d.__missing__(1))

# usign hte list as a defult_factory 
l = [1,2,3,'person' , 'atharva']
d = defaultdict(list)
for i in l: 
    d[i] = i
    
print(d)
d['person']=  'person_2'
print(d)
del d
d = defaultdict(list)
for i in l: 
    d[i].append(i)
print(d)
d['person'].append('person_2')
print(d)
print(d[12])    # use of default dict , gives us no keyvalue error 

# using int as defualt_factory 
l = [1,2,3,2,3,4,3,4,5]
d= defaultdict(int)
for i in l:  
    d[i] = d[i] + 1

print(d)

