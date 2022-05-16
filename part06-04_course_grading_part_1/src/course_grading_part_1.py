if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[int(parts[0])] = parts[1].strip() + " " + parts[2].strip()


exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        parts = [int(part) for part in parts]
        exercises[parts[0]] = sum(parts[1:])

for pic, student in students.items():
    if pic in exercises:
        total = exercises[pic]
        print(student, end=" ")
        print(total)
