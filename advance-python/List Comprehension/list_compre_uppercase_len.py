#a list containing tuples of the uppercase version and the length of the following words

# return a tuple of word toUpperCase and it length .i.e. ('HELLO', 5)
def upper(x): 
        return (x.upper(),len(x))

words = ["hello", "my", "name", "is", "Sam"]
#iter to create a list of upperCase letters & it length
# which is stored in the list <- upperCase ->
upperCase = list(upper(word) for word in words) 
print(upperCase)

