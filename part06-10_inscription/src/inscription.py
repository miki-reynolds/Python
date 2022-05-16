name = input("Whom should I sign this to: ")
where = input("Where shall I save it: ")

with open(where, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")