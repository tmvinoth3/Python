#code
a = [[1,2],[3,4]] 
b = a[:]
print(a)
print(b)
print(a[0])#same
print(b[0])#same ie a[0]=b[0]
a[0] = [5,6] #a[0] is changed
print(a[0])
print(b[0])#b[0] remains unchanged if modified
a[1].append(7)
print(a)
print(b)#again same results if appended