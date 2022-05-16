from datetime import*

file = input("Filename: ")
with open(file, "w") as diary:

    start = input("Starting date: ")
    add = int(input("How many days: "))
    start = start.split(".")
    start = datetime(int(start[2]), int(start[1]), int(start[0]))

    print("Please type in screen time in minutes on each day (TV computer mobile):")
    dict = {}
    total = 0
    for i in range(add):
        date_diary = start + timedelta(days = i)
        date_diary = date_diary.strftime("%d.%m.%Y")
        screentime = input(f"Screen time {date_diary}: ")
        pieces = screentime.split()
        sum = int(pieces[0]) + int(pieces[1]) + int(pieces[2])
        total += sum
        dict[f"{date_diary}: "] = screentime.replace(" ", "/")
    

    ave = total/add
    start_diary = start.strftime("%d.%m.%Y")
    end_diary = start + timedelta(days = (add-1))
    end_diary = end_diary.strftime("%d.%m.%Y")
    diary.write(f"Time period: {start_diary}-{end_diary}\n")
    diary.write(f"Total minutes: {total}\n")
    diary.write(f"Average minutes: {ave:.1f}\n")
    for key, value in dict.items():
        line = key + value
        diary.write(line + "\n")

    print(f"Data stored in file {file}")



