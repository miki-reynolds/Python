word = input("Please type in a word: ")
letter = input("Please type in a character: ")
index_start = word.find(letter)
index_end = 3 + word.find(letter)
if letter in word and len(word)>= index_end:
    print(word[index_start:index_end])
