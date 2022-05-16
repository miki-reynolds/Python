import re

def is_dotw(word: str):
    d = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.match(d, word):
        return True
    else:
        return False

def all_vowels(word: str):
    vowels = "^[aeiuoy]+$"
    if re.match(vowels, word):
        return True
    else:
        return False

def time_of_day(word: str):
    if re.match("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]", word) or re.match("2[0-3]:[0-5][0-9]:[0-5][0-9]", word):
        return True
    else:
        return False


# print(is_dotw("Mon"))

