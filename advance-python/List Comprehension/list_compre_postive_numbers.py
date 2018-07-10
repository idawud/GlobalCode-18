#list of positive numbers

# return a pos number thus GREATER THAN zero(0)
def pos(x):
    if x > 0:
        return x
#removes all value of type <- None ->     
def val(s):
    if s != None:
        return s
    
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#first iter & remove negative numbers
positive = list(pos(num) for num in numbers)
#then scrape off all value of type <- None -> 
fPos = list(filter(val,positive))
print(fPos)