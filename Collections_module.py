# Collectios module 

# counter 
from collections import Counter 

# With requence of items 
print(Counter(['B' , 'B' , 'A' , 'B' , 'C' , 'A' , 'B' ,'B' , 'A' ,'C']))

# dictionry 
print(Counter({'A' : 3  , 'B': 5 ,'C' : 2}))

# with keyword arguments 
print(Counter(A=3, B=5 , C=2 ))

# Ordered Dict 
from collections import OrderedDict

print("This is dictionaty ")
d  = {} 
d['a'] =1
d['b'] = 2
d['c'] = 3
d['d'] = 4 

for key,value in d.items() : 
    print(key, value )


# An ordered dictionary remembers the order in which the items 
# were inserted in the dictionary 

print("This is ordered dictionary : ")
od = OrderedDict()
od['a'] = 1
od['B'] = 2
od['C'] = 3
od['D'] = 4 

for key , value in od.items() : 
    print(key , value )

od = OrderedDict()
od['A'] = 1
od['B'] = 2 
od['C'] = 3 
od['D'] = 4 

print("Before Deleting ")
for key ,value in od.items() : 
    print(key, value ) 

# deleting element
od.pop('A')

# While deleting and re-inserting the same key , will pus hthe key to the last 
# to maintain order of insertion of the key
# Re-inserting the same 
od['A'] = 1

print("After re-inserting ")
for key , value in od.items() : 
    print(key, value)

# Delete Dict 
# Defualt Dict never raises keyError 

from  collections import defaultdict 
# Defining the dictionary 
d = defaultdict(int )
l = [1,4,2,1,4,2,6]

# iterate through rthe list 
# for keeping the count 
for i in l: 
    # the default value is 0
    # so there is not need to 
    # enter the key first 
    d[i] = d[i]+1 

print(d)

# Defining a dictionry 
d = defaultdict(list)

for i in range(5): 
    d[i].append(i)

print("Dictionary with vlues as list ")
print(d)

list2 = [1,5,2,4,3,5,1,4,2]
d = defaultdict(list)

for i in list2 : 
    d[i].append(i)

print(d)

# Chain map
# A chain map excalsulates many dicionaries into a single unot and returns a 
# list of dictionaries 

from collections import ChainMap

d1 = {'a' : 1 , 'b' : 2 , 'c' : 3}
d2 = {'c' : 3 , 'd'  :4}
d3 = {'e' : 5 , 'f': 6 , 'a' : 7}

# Definning the chainmap
c = ChainMap(d1 , d2,d3)
print(c)

# accessing elements, keys and values frm a chain
# map 
print(c['a'])
print(c['c'])

# using values ()
print(c.values())

# Accessing key s using keys()
print(c.keys())

# Adding a new dictionary 
import collections 

# print the chain map 
print("All the ChainMap contents : ")
print(c)

d4 = {'e': 10 , 'j': 11}
# using hte new_child() to add new dictionary 
c1 = c.new_child(d4)

# print the chain map 
print(c1)
# c1 is the new chainmap that contains d4 dictionary 
# the dicionary will get added at the front of the previous 
# dicionary 


# Named Tuple 



