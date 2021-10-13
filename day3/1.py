# arrays 
import array as arr 

a = arr.array('i' , [1,2,3])
print(a)
for j in a : 
    print(j)
    
a.append(12)
print(a)
a.insert(5 ,12)
print(a)

# a.append(1.2) gives error 
# because only one data type can be stored in the array 

a.remove(12)
print(a)
a.pop()
print(a)
print(a[::-1])
print(a.index(2))