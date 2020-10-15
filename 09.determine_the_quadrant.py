x,y= map(float,input("Enter X and Y: ").split())

if x > 0 and y > 0:
    print("The First Quadrant.")

elif x < 0 and y > 0:
    print("The Second Quadrant.")

elif x < 0 and y < 0:
    print("The Third Quadrant.")

elif x > 0 and y < 0:
    print("The Fourth Quadrant.")

elif x==0 and y==0:
    print("Point of origin")