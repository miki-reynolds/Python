def everything_reversed(strings: list):
    list =[]
    for word in strings:
        list.append(word[::-1])
    return list[::-1]
