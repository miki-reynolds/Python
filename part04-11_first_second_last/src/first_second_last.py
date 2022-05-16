
def first_word(sentence):
    list = sentence.split()
    return list[0]

def second_word(sentence):
    list = sentence.split()
    return list[1]

def last_word(sentence):
    list = sentence.split()
    return list[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))