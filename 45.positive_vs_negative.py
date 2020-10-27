import random
array=[]
for i in range(20):
    array.append(int(random.random()*20)-10)
# print(array)

pos=[]
neg=[]

for i in array:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)

print("Positive numbers: ", pos)
print("Negative numbers: ", neg)