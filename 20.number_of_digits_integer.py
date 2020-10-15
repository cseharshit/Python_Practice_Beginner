number=abs(int(input("Enter an integer: ")))

digit=1
number//=10
while number>0:
    number//=10
    digit+=1

print("The number of digits : ", digit)