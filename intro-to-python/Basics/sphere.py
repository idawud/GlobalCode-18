import math
 
# calculate surface area & volume of a sphere
radius = float(input("Enter the radius of the plane: "))
surfaceArea = 4 * math.pi *( radius **2)
print(" The Surface area is : " + str(surfaceArea))

volume = (4/3) * math.pi * pow(radius,3)
print(" The Volume is : " + str(volume))
