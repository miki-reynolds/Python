if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data ="exam_points1.csv"

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

exercises_points = {}
for key, value in exercises.items():
    exercises_points[key] = value//4

exam_points = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        parts = [int(part) for part in parts]
        exam_points[parts[0]] = sum(parts[1:])

heading = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
for header in heading:
    if header == heading[0]:
        print(f"{header:30}", end="")
    elif header == heading[-1]:
        print(f"{header:10}")
    else:
        print(f"{header:10}", end="")

for pic, student in students.items():
    if pic in exercises and exercises_points and exam_points:
        total = exercises_points[pic] + exam_points[pic]
        if 0 <= total <= 14:
            grade = 0
        if 15 <= total <= 17:
            grade = 1
        if 18 <= total <= 20:
            grade = 2
        if 21 <= total <= 23:
            grade = 3
        if 24 <= total <= 27:
            grade = 4
        if  total >= 28:
            grade = 5

        print(f"{student:30}", end=" ")
        print(f"{exercises[pic]:<10}", end=" ")
        print(f"{exercises_points[pic]:<10}", end=" ")
        print(f"{exam_points[pic]:<10}", end=" ")
        print(f"{(exercises_points[pic] + exam_points[pic]):<10}", end=" ")
        print(f"{grade:<10}")

# wrong format


