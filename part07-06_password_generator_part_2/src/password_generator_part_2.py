from random import*
from string import*

def generate_strong_password(length: int, c1: bool, c2: bool):
    pwd = ""
    special = "!?=+-()#"

    combo1 = ascii_lowercase + digits
    if c1 is True and c2 is False:
        pw = choice(ascii_lowercase) + choice(digits)
        for i in range(length-2):
            pw += choice(combo1)
        pw = list(pw)
        shuffle(pw)
        for i in pw:
            pwd += i

    combo2 = ascii_lowercase + special
    if c2 is True and c1 is False:
        pw = choice(ascii_lowercase) + choice(special)
        for i in range(length-2):
            pw += choice(combo2)
        pw = list(pw)
        shuffle(pw)
        for i in pw:
            pwd += i

    combo3 = ascii_lowercase + digits + special
    if c1 is True and c2 is True:
        pw = choice(ascii_lowercase) + choice(digits) + choice(special)
        for i in range(length-3):
            pw += choice(combo3)
        pw = list(pw)
        shuffle(pw)
        for i in pw:
            pwd += i
    
    if c1 is False and c2 is False:
        for i in range(length):
            pwd += choice(ascii_lowercase)

    return pwd

