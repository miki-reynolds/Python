n1 = int(input("Number 1:"))
n2 = int(input("Number 2:"))
operation = input("Operation:")
condition = operation == "add"
if condition:
    print(f"{n1} + {n2} = {n1 + n2}")

condition = operation == "multiply"
if condition:
    print(f"{n1} * {n2} = {n1 * n2}")

condition = operation == "subtract"
if condition:
    print(f"{n1} - {n2} = {n1 - n2}")
print("")