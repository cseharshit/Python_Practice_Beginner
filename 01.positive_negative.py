number=int(input("Enter a number: "))
if number > 0:
    print("{} is a positive number".format(number))
elif number < 0:
    print("{} is a negative number".format(number))
else:
    print("You entered 0")
