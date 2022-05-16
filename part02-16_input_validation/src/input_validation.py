from math import sqrt
while True:
    num = int(input("Please type in a number: "))
    if num == 0:
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(sqrt(num))
print("Exiting...")