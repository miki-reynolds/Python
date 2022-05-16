def generate_password(num: int):
    from string import ascii_lowercase
    alphabet = list(ascii_lowercase)
    result = ""
    from random import shuffle
    shuffle(alphabet)

    for letter in alphabet:
        result += letter

    return result[:num]
    
