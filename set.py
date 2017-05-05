#code
#set
s = {1,4,3,5,8,7,3}
print(s)#sorted in ascending order and remove duplicates

s.add(9) #adding values
print(s)

s.update([10,42]) #to update with existing
print(s)

s.remove(4) #remove(15) throws error 15 is not in set
print(s)

s.discard(1) #remove(15) not throw error
print(s)

t = s.copy() #copy references
print(t) 

u = set(t) #create using set constructor
print(u)
