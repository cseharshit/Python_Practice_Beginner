x=int(input("Enter the number: "))
y=int(input("Check whether {} is divisible by __:".format(x)))
if x%y==0: print("{} is divisible by {}".format(x,y))
else: print("{} is not divisible by {}".format(x,y))