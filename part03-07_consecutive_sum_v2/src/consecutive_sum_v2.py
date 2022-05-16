limit = int(input("Limit: "))
number = 1
summ = 1
numbers = "1"
while summ < limit:
    number += 1
    summ += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {summ}")


# limit = int(input("Limit:"))
# base = 0
# num = 1
# num_total = 0
# calculation = 'The consecutive sum: '
# while base < limit:
#     calculation += f"{num} + "
#     base += num
#     num += 1

# print(f"{calculation[:-3]} = {base}")
