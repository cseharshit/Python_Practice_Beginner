import random
x=[]
for i in range(20):
    x.append(int(random.random()*100))
print(x)

even=odd=0

for i in x:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Even numbers: ", even)
print("Odd numbers: ", odd)