from random import randint
x=int(input("Enter length of the array: "))
y,z=map(int, input('Enter range of numbers (a b) ').split())
array=[]

for i in range(x):
    array.append(randint(y,z))

print(array)

minimum=array[i]
for i in array:
    if i < minimum:
        minimum=i

print("Minimum number in the array: ", minimum)

#min(array)
