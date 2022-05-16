list = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        break

    name = input("name: ")
    if command == 1:
        if name not in list:
            print("no number")
        else:
            print(list[name])
        continue

    number = input("number: ")
    if command == 2:
        list[name] = number
        print("ok!")

print("quitting...")


