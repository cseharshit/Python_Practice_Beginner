#Multiplication_Table
x=1
a,b=map(int,input("Enter x and y: ").split())
while x<=a:
    y=1
    while y<=b:
        print("%4d" %(x*y),end="")
        y+=1
    print()
    x+=1
