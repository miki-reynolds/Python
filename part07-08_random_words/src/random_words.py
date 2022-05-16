from random import sample
def words(n: int, beginning: str):
    dict = []
    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            dict.append(line)
    
    list = []
    for item in dict:
        if item[:len(beginning)] == beginning:
            list.append(item)
    sel = sample(list, n)
    return sel

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)