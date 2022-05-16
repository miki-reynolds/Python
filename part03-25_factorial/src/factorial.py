while True:
    number = int(input("Please type in a number: "))
    i = number-1
    new = number*i
    if number > 1:
        while i-1 >= 1:
            new = new*(i-1)
            i-=1
        print(f"The factorial of the number {number} is {new}")
    elif number <= 0:
        print("Thanks and bye!")
        break
    elif number == 1:
        print(f"The factorial of the number 1 is 1")
    continue