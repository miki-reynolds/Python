word = input("Please type in a string: ")
vowels = "aeo"
index = 0
while index < len(vowels):
    vowel = vowels[index]
    if vowel in word:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
    
# word = input("Please type in a string: ")
# sub1 = "a"
# while True:
#     if "a" in word:
#         print("a found")
#     else:
#         print("a not found")

#     if "e" in word:
#         print("e found")
#     else:
#         print("e not found")

#     if "o" in word:
#         print("o found")
#     else:
#         print("o not found")
#     break
    
    

