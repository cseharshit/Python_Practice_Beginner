import math

perpendicular= float(input("Enter the length of Perpendicular: "))
base=float(input("Enter the value of Base: "))

hypotenuse=math.sqrt((pow(perpendicular,2)+pow(base,2)))

Area=(perpendicular*base)/2
Perimeter=perpendicular+base+hypotenuse

print("Area = ", Area, " Perimeter = %.2f"%Perimeter)

