def length_of_longest(names: list):
    longest = 0
    for item in names:
        if len(item) > longest:
            longest = len(item)
    return longest