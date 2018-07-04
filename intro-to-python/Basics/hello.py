import math
import datetime
"""""
 # converting degree to radian  
rad = 32  * ( math.pi / 180)
print(" 32 degrees in Radian is : " + str(rad))
print("\n")
"""""
"""""
# calculate surface area & volume of a sphere
radius = float(input("Enter the radius of the plane: "))
surfaceArea = 4 * math.pi *( radius **2)
print(" The Surface area is : " + str(surfaceArea))

volume = (4/3) * math.pi * pow(radius,3)
print(" The Volume is : " + str(volume))
""""
# date printing 
localtime = datetime.datetime.now()
print ("Current time is : ", localtime)

"""""
# word spliting
sentence= """Write a function called calculate that takes one string and two int arguments. The string should be "add", "subtract", "multiply" or "divide", or any of those words in uppercase"""
split = sentence.split(" ")
print(split)
print("\n")
"""""
# joining sentemces
#using the string.join(list) function
str0 = " "
str1 = ["Hello" ," Dawud", " how are u"]
join = str0.join(str1)
print(join)

# using a for loop to itereate & concactenate the words 
join1=""
for item in str1:
	join1 += item + " "

print(join1)

