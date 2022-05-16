words = input("Please type in a sentence: ")
index = 0
# space = words.find(" ")
print(words[index])
while index < len(words):
    if words[index] == " ":
        print(words[index+1])
    index += 1
    
    