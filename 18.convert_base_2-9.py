number1=int(input("Insert number to convert: "))
base_number=int(input("Choose the base to convert to from 2 to 9: "))

if not(2<=base_number<=9):
    quit()

number2=''
while number1>0:
    number2=str(number1%base_number)+number2
    number1//=base_number

print(number2)