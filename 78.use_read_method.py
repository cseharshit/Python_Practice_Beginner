fp = open('./data/Python.txt')
data = fp.read()
fp.close()

print(repr(data))

data = data.split('\n')
print(data)
