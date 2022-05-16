# Fix the program
points = int(input("How many points are on your card? "))
condition = points < 100
if condition:
    points_1 = points * 1.1
    print("Your bonus is 10 %")
    print("You now have", points_1, "points")
condition = points >= 100
if condition:
    points_2 = points* 1.15
    print("Your bonus is 15 %")
    print("You now have", points_2, "points")