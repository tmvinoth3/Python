#code
for i in range(0,5):
    print(i)
print(list(range(5,10)))#create list [5,6,7,8,9]
print(list(range(0,10,2)))#create list with difference 2
t = [10,20,30,40]
for i in enumerate(t):
    print(i) #Results count and value
#(0, 10)
#(1, 20)
#(2, 30)
#(3, 40)
for count,value in enumerate(t): #another way
    print("Count -",count,"Value -",value);