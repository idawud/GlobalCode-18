import functools
#x = lambda word, message: word + " "+ message

#list to key the words to be joined
words = ["Hello","World,", "I'm", "Dawud!"]

#func to return sum of all words in the list
def join_strings(words):
    return functools.reduce(lambda word, message: word + " "+ message, words)
 
# func join_strings(words) call and print
mess = join_strings(words)
print(mess)
