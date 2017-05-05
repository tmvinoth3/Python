#code
def minmax(items):
    print("Length =",len(items))
    return min(items),max(items)


lower, upper = minmax([2,35,48,5,7,3])
a,b = 2,3
a,b = b,a
print("a=",a,"b=",b)
print("min=",lower,"max=",upper)