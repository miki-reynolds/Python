from datetime import datetime, timedelta
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

dob = datetime(year, month, day)
compare = datetime(1999, 12, 31)
difference = compare - dob

if year < 2000:
    print(f"You were {difference.days} days old on the eve of the new millennium.")

else:
    print("You weren't born yet on the eve of the new millennium.")