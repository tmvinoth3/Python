#code
from pprint import pprint as pp #to print dict isotopes
#Dict key,value pair
name_and_age = [('ram',21),('sam',21),('john',21),('jane',21)]
d = dict(name_and_age)
print(d)

#another way
d1 = dict(a='alfa',b='bravo',c='charlie',d='delta')
print(d1)

#d.copy()--to copy
d.update(d1)
print(d) #upate with d1 data

#dict are iterable
for item in d:
    print("{} => {}".format(item,d[item]))
    
#to iterate only values
for item in d1.values():
    print(item)
    
#to iterate only keys Default is keys
for item in d1.keys():
    print(item)
    
#to iterate only key,values items
for k,v in d1.items():
    print("{} => {}".format(k,v))
    
#dict can be updated
d1['a'] = ['beta']
print(d1['a'])

#another way of defining dict
d2 = {'a' : 1,
        'b':2}
pp(d2)

