x = ['a','b','c','d','e']
y = input("Insert an alphabet: ")

if y in x:
    print(1)
else:
    raise ValueError("Letter does not exist!")

