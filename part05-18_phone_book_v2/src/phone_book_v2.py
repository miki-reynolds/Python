def command_search(directory: dict):
    name = input("name: ")
    if name in directory:
        numbers = directory[name]
        for number in numbers:
            print(number)
    else:
        print("no number")

def command_add(directory: dict):
    name = input("name: ")
    number = input("number: ")
    if name not in directory:
        directory[name] = []
    directory[name].append(number)
    print("ok!")
    return directory

def main():
    directory = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            break
        elif command == 1:
            command_search(directory)
        elif command == 2:
            command_add(directory)
    print("quitting...")

main()