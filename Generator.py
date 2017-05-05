#code
#Generators
#function return as whole iterate through next()

def gen123():
    print("yield 1")
    yield 1 
    print("yield 2")
    yield 2 
    print("yield 3")
    yield 3 
    print("About to return")

g = gen123()
print(next(g))