def separate_characters(my_string: str):
    import string
    first = ""
    second = ""
    third = ""

    for letter in my_string:
        if letter in string.ascii_letters:
            first += letter
        if letter in string.punctuation:
            second += letter
        if letter not in string.ascii_letters and letter not in string.punctuation:
            third += letter
    return (first, second, third)

# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])