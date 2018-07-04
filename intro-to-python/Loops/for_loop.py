for i in range(1,11):
    print (i)
print("\n")
# for in loop iter
for j in [1, 2, 3]:
    print (j)
print("\n")
# range with increment
for j in range(0,20,2):
    print (j)
print("\n")

aList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for num in aList:
	print(num)
print("\n")

#print a square of stars
def squareStar():
	for star in range(0,4):
		print( 4 * "*" )
squareStar()
print("\n")

# print an arrow head
def arrowHead():
	for arr in range(1,5):
		print( arr * "*")
	for head in range(3,0,-1):
		print(head * "*")
arrowHead()
print("\n")
