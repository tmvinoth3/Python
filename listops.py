#code
a = [2,4,'the',"the","the"]
print(a*3) #list repetition [2, 4, 2, 4, 2, 4]
#create list with 3 indexes 0,1,2 and all indices point
#to a
print(a.index(4))
print(a.count('the'))
del a[1] #delete
print(a)
a.remove(a[2])
print(a)
a.insert(0,'new')
print(a)