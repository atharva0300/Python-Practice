s = input("Enter : ")
result = s.endswith('person')
print(result)
result = s.startswith('here')
print(result)
print(s)
result= s.replace('h' , '.', 2)
print(result)
result = s.replace('a' , '.')
print(result)

tuple1 = ()
print(tuple1)
result = tuple("athava" ,) *3
print(result)
result = ()
result = ('atharva' ,)*3
print(result)
a,b,c = result
print(a , b , c)
print(tuple('atharva' ,)*3)

s = tuple([1,2,3])
result = result + s
print(result)
del s 
print(result)
print(result.count('atharva'))
print(result.index('atharva'))
print(len(result))
print(enumerate(result))
result = ('atharva', 'is ' , 'a' , 'person')
print(max(result))
print(min(result))
print(sorted(result))
