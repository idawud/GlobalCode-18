# returns value if it is an Even
def is_even(x):
    if x % 2 == 0:
        return x

originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#using the filter func, each value in originalList is tested
# even if true add to the newList
newlist = list(filter(is_even,originalList))

#print the two lists
print("The original list: {}".format(originalList))
print("The filtered list: {}".format(newlist))