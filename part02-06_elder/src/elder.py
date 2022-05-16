print("Person 1:")
per1 = input("Name: ")
age1 = int(input("Age: "))
print("Person 2:")
per2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {per1}")
elif age1 == age2:
    print(f"{per1} and {per2} are the same age")
else:
    print(f"The elder is {per2}")
    