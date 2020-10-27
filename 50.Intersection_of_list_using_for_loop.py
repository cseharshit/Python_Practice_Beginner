x=[1,3,6,[3,6,7],'ab','c','u',5]
y=[8,19,123,6,1,'ab',[3,6,7]]
z=[]


for i in x:
    for j in y:
        if i == j:
            z.append(i)
            break

print(z)