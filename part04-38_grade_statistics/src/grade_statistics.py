# exam_points = []
# exercises = []
# while True:
#     points = input("Exam points and exercises completed: ")
#     if points != "":
#         point_split = points.split()
#         exam_points.append(int(point_split[0]))
#         exercises.append(int(point_split[1]))
#     else:
#         break
# print("Statistics:")

# exercises_points = []
# for excercise in exercises:
#     exercises_points.append(int(excercise/10))


# # exam_points = [15, 10, 11, 4]
# # exercises_points = [8, 5, 4, 1]

# grades = []
# sum = 0
# for i in range(len(exam_points)):
#     total = exam_points[i] + exercises_points[i]

#     if total < 15:
#         grades.append(0)
#     elif 15 <= total <= 17:
#         if exam_points[i] < 10:
#             grades.append(0)
#         else:
#             grades.append(1)
#     elif 18 <= total <= 20:
#         if exam_points[i] < 10:
#             grades.append(0)
#         else:
#             grades.append(2)
#     if 21 <= total <= 23:
#         if exam_points[i] < 10:
#             grades.append(0)
#         else:
#             grades.append(3)
#     if 24 <= total <= 27:
#         if exam_points[i] < 10:
#             grades.append(0)
#         else:
#             grades.append(4)
#     if 28 <= total <= 30:
#         if exam_points[i] < 10:
#             grades.append(0)
#         else:
#             grades.append(5)

#     sum+= total

# print(f"Points average: {sum/len(grades)}")
# pas = ( (len(grades) - grades.count(0) ) / len(grades) )*100
# print(f"Pass percentage: {pas:.1f}")

# print("Grade distribution:")
# list = [5, 4, 3, 2, 1, 0]
# for i in list:
#     print(str(i) +":",end=' ')
#     count = grades.count(i)
#     print(count*"*")
grades = [0] * 6
print(grades)
