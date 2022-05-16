word = input("Please type in a word: ")
sub = input("Please type in a character: ")
start = 0

while start + 3 <= len(word):
    if sub == word[start]:
        print(word[start:start+3])
    start += 1



# word = word = input("Please type in a word: ")
# character = input("Please type in a character: ") 
# index = word.find(character)
# while index!=-1:
#     if len(word)>=index+3:
#         print(word[index:index+3])
#     index = word.find(character,index+1)
        

    
    

    