#Print a multiplication Table using for loop
a,b=map(int,input("Enter rows and columns: ").split())
for x in range(1,a+1):
    for y in range(1,b+1):
        print("%4d" %(x*y), end="")
    print()