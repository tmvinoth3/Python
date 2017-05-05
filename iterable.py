#code
#iterable objects passed into the built-in iter() function

iterable = ['this','is','list']

iterator = iter(iterable)

#iterator objects passed into the built-in next() method 
le = int(len(iterable))
while(le):
        print(next(iterator))
        le-=1
