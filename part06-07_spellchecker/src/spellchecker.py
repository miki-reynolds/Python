if True:
    sentence = input("Write text: ")
else:
    sentence = " We use ptython to make a spell checker"

string = sentence.lower().split()

dictionary = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        dictionary.append(line)

for word in string:
    if word not in dictionary:
        sentence = sentence.replace(word, "*" + word + "*")

print(sentence)





