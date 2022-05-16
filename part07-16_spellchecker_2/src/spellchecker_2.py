from difflib import*

contents = []
with open("wordlist.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        contents.append(line)

words = input("write text: ")
list = words.lower().split()
wrong = []
for word in list:
    if word not in contents:
        wrong.append(word)
        words = words.replace(word, f"*{word}*")
print(words)

print("suggestions:")
for word in wrong:
    print(word + ":", end=' ')
    close = get_close_matches(word, contents)
    string = ", ".join(close)
    print(string)
