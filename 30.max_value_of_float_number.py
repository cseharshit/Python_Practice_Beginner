from random import random

x=round(random()*1000,3)

print(x)

y = str(x)
maxi = -1

for i in range(len(y)):
    if y[i]== '.':
        continue
    elif maxi < int(y[i]):
        maxi = int(y[i])
    
print(" The maximum element is = ", maxi)