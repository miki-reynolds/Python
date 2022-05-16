def add_student(students: dict, name: str):
    students[name] = None
    return students

def print_student(students: dict, name: str):
    if name in students:
        print(name + ":")
        print(" ", end="")
        if students[name] == None:
            print("no completed courses")
        else:
            print(f"{len(tuple)} completed courses:")
            print(" ", end="")
            print("average grade {tuple[1]+tuple[]")

    else:
        print(name + ":", end=" ")
        print("no such person in the database")

def add_course(students: dict, name: str, (course: str, num: int)):
    students[name] = (course, num)
    return students

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")