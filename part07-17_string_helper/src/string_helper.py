import string
def change_case(orig_string: str):
    a= ""
    for letter in orig_string:
        if letter.isupper():
            a += letter.lower()

        elif letter.islower():
            a += letter.upper()
        else: 
            a+= letter
            
    return a
# change_case("AAAaaa")





def split_in_half(orig_string: str):
    bpoint = (len(orig_string)//2)
    first = orig_string[:bpoint]
    second = orig_string[bpoint:]

    return (first, second)

def remove_special_characters(orig_string: str):
    for letter in orig_string:
        if letter != " ":
            if letter not in string.ascii_letters and letter not in string.digits:
                orig_string = orig_string.replace(letter, "")
    return orig_string       

# print(remove_special_characters("This is a test, lets see how it goes!!!11!"))

