# simple while loop to print between 0 and 10
i = 0
while(i < 10):
    i = i + 1
    print (i)

# for while in range print 
val = 12
while(val< 20):
    print(val)
    val = val +1

# The  even while loop
def evens(num1,num2):
    one = num1
    while(one < num2): 
        if(one % 2 ==0):
            print(one)
        one = one +1

evens(0,40)

# The REVERSE even while loop
def reverse_evens(num1,num2):
    two = num2
    while(two > num1): 
        if(two % 2 ==0):
            print(two)
        two = two - 1
reverse_evens(0,20)
