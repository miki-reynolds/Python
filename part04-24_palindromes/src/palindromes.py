def palindromes(string: str):
    return string == string[::-1]

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            break
        else:
            print(f"that wasn't a palindrome")

    print(f"{word} is a palindrome!")

main()
# if __name__== "__main__" :
#     # main()