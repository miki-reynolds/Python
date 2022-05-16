def largest():
    with open("numbers.txt") as new_file:
        contents = new_file.read()
        numbers = contents.split()
        biggest = int(max(numbers))
        return biggest

if __name__ == "__main__":
    print(largest())
