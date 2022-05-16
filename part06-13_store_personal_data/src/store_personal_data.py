def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        line =""
        for data in person:
            line += f"{data};"
        line = line[:-1]
        file.write(line+"\n")

# store_personal_data(("Paul Paulson", 37, 175.5))
