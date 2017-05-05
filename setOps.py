#code
#set operations
a = {1,2,3,4,5}
b= {3,5,1,6,7}
c = {1,2}
d={8,9}

print(a.union(b)) #Results {1, 2, 3, 4, 5, 6, 7}

print(a.intersection(b)) #{1, 3, 5}

print(a.difference(b)) #{2, 4}

print(a.symmetric_difference(b)) #{2, 4, 6, 7}

print(c.issubset(a)) #True

print(a.issuperset(c)) #True

print(a.isdisjoint(d)) #True