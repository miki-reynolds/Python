def most_common_character(string: str):
    count = 0
    for i in range(len(string)):
        if string.count(string[i]) > count:
            count = string.count(string[i])
            word = string[i]
    return word
