def no_shouting(strings: list):
    lower = []
    for item in strings:
        if not item.isupper():
            lower.append(item)
    return lower
            
