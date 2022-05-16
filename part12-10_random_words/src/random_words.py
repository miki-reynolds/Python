from random import choice

def word_generator(characters: str, length: int, amount: int):
    i = 0
    for i in range(amount):
        word = ""
        for j in range(length):
            word += choice(characters)
        yield word

# wordgen = word_generator("abcdefg", 3, 5)
# for word in wordgen:
#     print(word)

