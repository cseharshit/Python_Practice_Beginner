num = int(input("Insert some numbers: "))

even = 0
odd = 0

while num > 0:
    if num%2 == 0:
        even += 1
    else:
        odd += 1
    num = num//10
print("Even numbers = %d, Odd numbers = %d" % (even,odd)) 
