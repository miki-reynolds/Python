def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
    
def triangle(size):
    i = 0
    while i <= size:
        line(i, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
