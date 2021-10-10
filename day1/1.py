string = "here"
print(string)
for i in range(len(string )): 
    print(string[i])
print()
for i in range(-len(string)+1 , 1):
    print(string[i])

print()
del string 
s = "i\'am"
print(s)

s = "{} {} {}" .format('12' , 'atharva' , 'here')
print(s)

s = "{0} {2} {1} " .format('12' , 'atharva' , 'here')
print(s)

s = "{a} {b} {c} " .format(a=  'atharva' , b = 'pingale' , c = 'is a person')
print(s)

# binary repreesentation of a string 
s = "{0:b}" .format(12)
print(s)

s = "{0:e}" .format(12.123)
print(s)

s= "{0:.2f}" .format(1/2)
print(s)

s = "|{:<10}|{:^10}|{:>10}|" .format('atharva' ,'pingale' , 'is here')
print(s)

i = 12.12345567;
print("%3.2f" %i)

i= 123.456
print("%0.6f" %i)
