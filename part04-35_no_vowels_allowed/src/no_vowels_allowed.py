def no_vowels(string: str):
    vowels ="a,e,i,o,u"
    for item in string:
        if item in vowels:
            string = string.replace(item, "")
    
    return string