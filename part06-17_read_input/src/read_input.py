def read_input(number: input, n1: int, n2: int):
    while True:
        try:
            num = int(input(number))
            if n1 <= num <= n2:
                return num

        except ValueError:
            pass
        print(f"You must type in an integer between {n1} and {n2}")

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)

