#code
#Fibonacci
a,b,i=-1,1,0
while(i<7):
    print(a+b)
    a,b = b,a+b 
    i+=1
    