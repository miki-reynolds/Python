while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    cmmd = int(input("Function: "))

    if cmmd == 1:
        fin = input("The word in Finnish: ")
        eng = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            line = f"{fin} - {eng}"
            file.write(line + "\n")
        print("Dictionary entry added")

    elif cmmd == 2:
        dict = []
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                dict.append(line)

        for item in dict:
            if search in item:
                print(item)

    elif cmmd == 3:
        break
print("Bye!")
