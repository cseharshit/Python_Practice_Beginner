from random import randint

x=int(input("Enter number of elements: "))
arr=[randint(1,100) for i in range(x)]
print(arr)

j=x-1
while j!=0:
    k=0
    for i in range(1,j+1):
        if arr[i] > arr[k]:
            k=i
        # Swap the values
    arr[k],arr[j]=arr[j],arr[k]
    j-=1

print(arr)