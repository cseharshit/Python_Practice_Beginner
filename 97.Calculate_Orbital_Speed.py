from math import pi

radius=float(input("Enter radius of the orbit(million km): "))
orbital_speed=float(input("Insert orbital speed(km/s): "))

radius=radius*1000000
year=(2*pi*radius/orbital_speed)/(60*60*24)
print(round(year), " years")