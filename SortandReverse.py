#code
l = [2,1,5,4,3]
m = l.copy()
str = 'this is string'
strlist = str.split() #string to list
m.sort()#sort
print(l)

m.reverse() #reverse
print("m : ",m)

l.sort(reverse=True)
print("l : ",l)#reverse

strlist.sort(key=len) #sort list
print(strlist);

print('*'.join(strlist)) #convert to string

n = sorted(l) #not change the l
print(n)
r = reversed(n) #not reverse the n
print(r)