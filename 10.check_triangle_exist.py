print("Enter the length of the proposed triangle:\n")
x=float(input("x :"))
y=float(input("y :"))
z=float(input("z :"))

if x+y>z and x+z>y and y+z>x:
    print("Triangle Exist with sides {},{},{}".format(x,y,z))

else: 
    print("Triangle does not exist")
