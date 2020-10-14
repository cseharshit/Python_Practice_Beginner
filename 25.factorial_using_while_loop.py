num = abs(int(input("Insert any number: ")))

factorial =1
while num > 1:
    factorial *= num
    num -= 1
    
print ("The result of factorial = ", factorial)