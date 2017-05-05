#code
s = "this is List sequence example".split() #string to list
print(s[2]) #access by index "sequence"
print("Negative index : ",s[-1]) #last element is at -1 index(Negative Index)
print("Positive to Negative Index : ",s[1:-1]) #prints "is" b/w first element(1) and last element(-1)
print("Last element Optional :", s[2:])#prints all elemens from first
print("First element Optional :", s[:2])#prints all elements till last
print("both elements Optional :", s[:])#prints all elements
t = s[:2]+s[2:]
print("Two Half Lists ",t) #adding two half lists
v = s.copy();
print("Copy :", v); #copy list
u = list(s)
print("List constructor :", u) #using list constructor
