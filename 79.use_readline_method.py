fp = open('./data/Python.txt')
data = []

i = fp.readline()
while i != '':
    data.append(i)
    i = fp.readline()
fp.close()
print(data)