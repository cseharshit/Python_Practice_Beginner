from random import randint
x=int(input("Enter length of the array: "))
y,z=map(int, input('Enter range of numbers (a b) ').split())
array=[]

for i in range(x):
    array.append(randint(y,z))

print(array)

maximum=0
for i in array:
    if i > maximum:
        maximum=i

print("Maximum number in the array: ", maximum)

#max(array)
