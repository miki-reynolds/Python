def longest(strings: list):
    max = ""
    for item in strings:
        if len(item) > len(max):
            max = item
    return max 


