goods={}
for i in open("./data/Program82.txt"):
    categories=i.split()
    categories[1]=float(categories[1])
    categories[2]=float(categories[2])
    goods[categories[0]]=[categories[1],categories[2]]

print(goods)