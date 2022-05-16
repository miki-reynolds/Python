

def spruce(number):
    print("a spruce!")
    i = 0
    j = number
    while i < (number*2):
        print(" "*(j-1), end='')
        print(i*"*" + "*")
        i += 2
        j -= 1
    print(" "*(number-1), end='')
    print("*")
if __name__ == "__main__":
    spruce(3)


# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *