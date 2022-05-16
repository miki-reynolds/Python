def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def shape(size1, character1, size2, character2):
    i = 0
    while i <= size1:
        line(i, character1)
        i += 1

    row = size2
    while row > 0:
        line(size1, character2)
        row -= 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")