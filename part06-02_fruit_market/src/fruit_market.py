def read_fruits():
    with open("fruits.csv") as new_file:
        list = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            cost = float(parts[1])
            list[fruit] = cost
        return list

if __name__ == "__main__":
    print(read_fruits())

