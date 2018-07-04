# Even & Odd
i = 9
if(i % 2 == 0):
    print( "Even Number")
else:
    print ("Odd Number")


# even sum return function
aList =[ 1,2,3,4,5,6,7,8,9,10,40]
def evens(listy):
	sum = 0
	for num in listy:
		if ( num%2 ==0):
			sum +=num
	return sum
 
val = evens(aList)
print(val)


#older or younger
myage = 22
def get_age():
	age = int (input("Enter your age: "))
	return age
userAge =  get_age()
if myage > userAge:
	print("I am Older,User is younger")
else:
	print(" User is older, am younger")


#age guesser
def get_yob():
	yob = int (input("Enter your year of Birth: "))
	return 2018 - yob
myYob = get_yob()
print("You are approximately " + str(myYob) + (" years old"))


# leap year
def leap_year():
	year = int (input("Enter your year of Birth: "))
	if ( year % 4 == 0  and year % 100 == 0  and year % 400 == 0):
 			print("You were born in a leap year")
	else:
		print("You were NOT born in a leap year")		
leap_year()






