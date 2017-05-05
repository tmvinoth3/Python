#code
#Exception Handling
def convert(s):
    try:
        x=int(s)
        print("Success")
    except (ValueError,TypeError):
        print("Conversion failure")
        x=-1
    return x
    
print(convert("33"))

print(convert("abc"))

print(convert([1,2]))