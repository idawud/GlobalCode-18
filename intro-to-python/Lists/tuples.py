def partition (num):
    if num % 2 == 0:
        tup = (num,None)
    else:
        tup = (None,num)
    return tup

a = partition (4)
print(a)


def partition_list(listy):
    even =[]
    odd = []
    result = []
    for item in listy:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    result.append(tuple(even))
    result.append(tuple(odd))
    return result

alist= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = partition_list(alist)
print(b)