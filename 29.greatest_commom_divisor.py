first_num = int(input("Insert first number: "))
second_num = int(input("Insert second number: "))

while first_num != 0 and second_num != 0:
    if first_num > second_num:
        first_num %= second_num
    else:
        second_num %= first_num
        
GCD = first_num + second_num
print("The greatest common divisor = ", GCD)

