print("Using the Lambda Function: \n")
# the Lambda Function also called an anonymous func,
# does not have a name and is called implicitly

originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#using the filter func & a Lambda Function, each value in originalList
#is tested even if true add to the newList
newlist = list(filter(lambda x: x % 2 == 0,originalList))

#print the two lists
print("The original list: {}".format(originalList))
print("The filtered list: {}".format(newlist))