sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
#print(words)

list1 = [len(word) for word in words]
print(list1)
list2 = [len(word) for word in words if word != "the"]
print(list2)

