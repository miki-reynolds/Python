import json
# filename = "file1.json"
def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    people = json.loads(data)

    for person in people:
        for header, info in person.items():
            if header == "name":
                print(person[header], end=" ")

            if header == "age":
                print(f"{person[header]} years", end=" ")
            
            elif header == "hobbies":
                print("(", end='')
                for h in person[header]:
                    print(h, end='' )
                    if h != person[header][-1]:
                        print(", ", end='')
                print(")")

        print()

# print_persons(filename)