import math

x,y= map(float,input("Enter x, y: ").split())
r = float(input("Enter the radius of the circle"))

h=math.sqrt(pow(x,2)+pow(y,2))
if h <=r:
    print("The point belongs to circle.")

else:
    print("The point does not belong to circle.")
