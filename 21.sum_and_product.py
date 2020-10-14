# This program is used to sum and multiply of the digits

num=abs(int(input("Insert integer value:")))
sum = 0
mul = 1

while num != 0:
    digit= num%10
    sum += digit
    mul *= digit
    
    num=num//10
    
print("Sum of digit = ",sum)
print("Product of digit = ",mul)
    