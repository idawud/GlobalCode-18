# function to return true if "a" is in the sentence
def letterSearch(sentence):
	for letter in sentence:
		if letter == "a":
			return True

sent = """Write a function that takes a string and returns True if the string contains the letter 'a', otherwise returns False. Don't use Python's in operator, write the code yourself!"""

val = letterSearch(sent)
print(val)

# function to return true if a letter  alpha " " is in the sentence
def letterSearch2(sentence,alpha):
	for letter in sentence:
		if letter == alpha:
			return True
val2 = letterSearch2(sent,'a')
print(val2)

# function to return true if "s" & "m" is found is in the sentence else false
def letterSearch3(sentence):
	let1=False 
	mtr=False
	for letter in sentence:
		if letter == "s":
			let1=True
		elif letter == "m":
			mtr =True
	if let1 and mtr:
		return True
	else:
		return False

val3 = letterSearch3(sent)
print(val3)

