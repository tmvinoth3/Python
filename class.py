#code
#classes
#class name CamelCase
class Flight:
    def __init__(self,number):#Initialize with value
        self._number = number
    
    def number1(self):
        return "TMV89"
    
    def number2(self):
        return self._number
    
    def sum(self,a,b):
        return a+b

f = Flight("TMV90") #set value through init
print(f.number1())
print(f.number2())

#Inheritance
class ship(Flight):#Inherits flight class
    pass
s = ship("TMV91")
print(s.sum(2,6))

# _(UnderScore) to ignore item
l = [1,2,3,4]
for _ in l:
    print(item)
