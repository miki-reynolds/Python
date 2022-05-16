def all_the_longest(strings: list):
    result = []

    for name in strings:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
    return result