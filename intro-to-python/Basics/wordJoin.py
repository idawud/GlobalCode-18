# joining words

#METHOD 1: using the string.join(list) function
str0 = " "
str1 = ["Hello" ," Dawud", " how are u"]
join = str0.join(str1)
print(join)

# METHOD 2:  using a for loop to itereate & concactenate the words 
join1=""
for item in str1:
	join1 += item + " "

print(join1)

