def shortest(strings: list):
    strings.sort(key = len)
    return strings[0]
