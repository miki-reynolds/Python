def invert(dictionary: dict):
    new = {}
    for key, value in dictionary.items():
        new[value] = key
    dictionary.clear()
    for key, value in new.items():
        dictionary[key] = value









        