from random import random

num=20
myList=[0]*num

for i in range(num):
    myList[i]=int(random()*50)
print(myList)

max_i=1
my_length=1
order=0

for i in range(1,num):
    if myList[i]>myList[i-1]:
        my_length+=1
    else:
        if my_length>max_i:
            max_i=my_length
            order = i
        my_length = 1
ordered_values=myList[order-max_i:order]
print("The maximum length = ", max_i)
print("Ordered values = ",ordered_values)