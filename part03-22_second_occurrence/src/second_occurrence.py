word = input("Please type in a string: ")
sub = input ("Please type in a substring: ")
index = word.find(sub) + len(sub)
word1 = word[index:]
n = word1.find(sub)
if word1.find(sub) != -1: 
    print(f"The second occurrence of the substring is at index {index + n}.")
else:
    print("The substring does not occur twice in the string.")