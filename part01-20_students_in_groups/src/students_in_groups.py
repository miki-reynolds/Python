students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
groups = students / size
if groups % 2 == 0:
    print(f"Number of groups formed: {groups}")
else:
    print(f"Number of groups formed: {int(groups) + 1}")