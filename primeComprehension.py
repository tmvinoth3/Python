#code
from math import sqrt
def IsPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
    return True

def main():
    inp = int(input())
    print([x for x in range(inp) if IsPrime(x)])#list compreh

if __name__ == '__main__':
    main()
print({x:x*x for x in range(101) if IsPrime(x)})#set compreh