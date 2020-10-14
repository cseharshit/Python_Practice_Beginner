from random import random
N = int(input("Enter the size of array: "))
array = []

for x in range(N):
    array.append(int(random()*100))
    
array.sort()
print(array)

number=int(input("Search for any number in the array: "))

min = 0
max = N-1

while min <= max:
    mid = (min + max) // 2
    if number < array[mid]:
        max = mid-1
    elif number > array[mid]:
        min = mid+1
    else:
        print("The number is located at index: ",mid)
        break
else:
    print("{} is not present in the array!".format(number))
    