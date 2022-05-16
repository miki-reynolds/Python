from functools import reduce

class CourseAttempt:
    def __init__(self, name: str, grade: int, credits: int):
        self.name = name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(courses):
    s = reduce(lambda total, item: total + item.credits, courses, 0)
    return s

def sum_of_passed_credits(courses):
    return reduce(lambda total, item: total + item.credits, filter(lambda x: x.grade >= 1, courses), 0)

def average(courses):
    students = list(filter(lambda x: x.grade >= 1, courses))
    return reduce(lambda total, item: total + item.grade, students, 0) / len(students)

# s1 = CourseAttempt("Introduction to Programming", 5, 5)
# s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
# s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
# ag = average_grade([s1, s2, s3])
# print(ag)