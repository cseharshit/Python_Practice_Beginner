import random

x=20
y=[]

avg=0

for i in range(x):
    y.append(int(random.random()*100))
    print("%d"%y[i],end=" ")
    avg+=y[i]
print()

avg=avg/x
print("Average = ", avg)

for i in y:
    if i>avg:
        print(i, end=" ")