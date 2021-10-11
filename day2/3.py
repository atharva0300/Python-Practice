
from functools import partial 

def power(a,  b): 
    return pow(a,b)


p = partial(power ,b=2)
print(p(12))
p2 = partial(power , b=3)
print(p2(12))
p3 = partial(power , 2)
print(p3(3))

print(p.func)
print(p.keywords)
print(p.args)

# partial method class

from functools import partialmethod 

class Base : 
    def __init__(self): 
        self.color = 'black'
    def _color(self , type):
        self.color = type 
    
    a = partialmethod(_color , type='red')
    b = partialmethod(_color, type = 'black')
    c = partialmethod(_color , type= 'green')


d = Base()
print(d.color)
d.a()
print(d.color)