#code
words = "This is string this".split()
print(words)

#list comprehension
print([len(word) for word in words]) #[4, 2, 6, 4]

#set comprehension no duplicates
print({len(word) for word in words})  #{2, 4, 6}

#dict comprehension
d = {'a':'abc','b':'bcd','c':'cde'}
print({item for item in d.items()})
print({x[0]:x for x in words})


