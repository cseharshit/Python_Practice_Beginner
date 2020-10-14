choice=''
while choice!='q':
    choice=input("Enter choice: +,-,*,/: ")
    if choice=='q':
        break
    if choice in ('+','-','*','/'):
        x=float(input("x = "))
        y=float(input("y = "))
        if choice=='+':
            print("%.2f" %(x+y))
        
        elif choice=='-':
            print("%.2f" %(x-y))
        
        elif choice=='*':
            print("%.2f" %(x*y))
        
        elif choice=='/':
            if y!=0:
                print("%.2f" %(x/y))
            else: print("Error! You cannot divide by zero")
    else:
        print("Invalid operator")
    choice=input('Press q to quit, any other key to continue: ')

    