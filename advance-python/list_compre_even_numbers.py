#list of even numbers

# return a number if even thus <- number % 2 == 0 ->
def pos(x):
    if x % 2 == 0:
        return x
#removes all value of type <- None ->     
def val(s):
    if s != None:
        return s

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
#first iter & remove all odd numbers
positive = list(pos(num) for num in numbers)
#then scrape off all value of type <- None -> 
fPos = list(filter(val,positive))
print(fPos)
