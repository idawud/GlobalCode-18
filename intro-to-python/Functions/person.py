def get_age():
	age = int (input("Enter your age: "))
	return age

def get_name():
	name = input("Enter your Name ")
	return name


userAge =  get_age()
userName = get_name()

print("Your name is {} and you are {} old".format(userName,userAge)) 
