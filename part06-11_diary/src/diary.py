while True: 
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))

    if function == 0:
        break
    elif function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as new_file:
            new_file.write(f"{entry}\n")
            
    elif function == 2:
        print("Entries: ")
        with open("diary.txt") as my_file:
            print(my_file.read())

print("Bye now!")

