def greatest_number(n1, n2, n3):
    list = [n1, n2, n3]
    greatest = max(list)
    return greatest
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)