def line(number, text):
    # number = int(input())
    # text = input("")
    if len(text) > 0:
        print(text[0]*int(number))
    else:
        print("*"*number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")