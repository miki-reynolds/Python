word = input("Please type in a string: ")
n = -1
while n >= -len(word):
    print(word[n:])
    n -= 1
    