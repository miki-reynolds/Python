def histogram(string: str):
    list ={}
    for letter in string:
        if letter not in list:
            list[letter] = ""
        list[letter] += "*"

    for key, value in list.items():
        print(f"{key} ", end='')
        print(value)