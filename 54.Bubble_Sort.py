from random import randint

x=int(input("Enter number of elements: "))
arr=[randint(1,100) for i in range(x)]
print(arr)

for i in range(x):
    for j in range(x-i-1):
        if (arr[j] > arr[j+1]):
            # Swap the values
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)