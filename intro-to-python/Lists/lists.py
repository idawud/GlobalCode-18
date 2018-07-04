list = []
list.append('a')
list.append('b')
print (list)

# list even return function 
def evenInRange(num1,num2):
	list = []
	for i in range(num1,num2):
		if i % 2 ==0:
			list.append(i)
	return list

print(evenInRange(2,22))
