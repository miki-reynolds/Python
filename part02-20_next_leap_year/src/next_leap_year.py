start_year = int(input("Year: "))
year = start_year + 1

# why doesnt it work when you put year += 1 up here or after while true?
# If we put year+=1 after/beofre while true, then we already miss the initial value of year to begin with?
while True:
    # Why didnt we put "and" for both 100 and 400? because that would mean it can also be divisible by 4...
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
    year += 1
# year += 1 down here so we can have a loop
print(f"The next leap year after {start_year} is {year}")

# while True:
#     year = int(input("Year: "))
#     # print("condition1:", year % 100 == 0 and year % 400 == 0)
#     if year % 100 == 0 and year % 400 == 0:
#         leap_year = year + 4
#         break

#     # print("condition2:", (year + 4) % 4 == 0 and (year + 4) % 100 == 0)
#     if (year + 4) % 4 == 0 and (year + 4) % 100 == 0:
#         leap_year = year + 8
#         break

#     # print("condition3:", year % 4 == 1)
#     if year % 4 == 1:
#         leap_year = year + 3
#         break

#     # print("condition4:", year % 4 == 2)
#     if year % 4 == 2:
#         if (year + 2) % 4 == 0 and (year + 2) % 100 == 0 and (year + 2) % 400 != 0:
#             if (year + 4) % 4 == 0:
#                 leap_year = year + 4
#             else:
#                 leap_year = year + 6
#         else:
#             leap_year = year + 2
#         break

#     # print("condition5:", year % 4 == 3)
#     if year % 4 == 3:
#         leap_year = year + 1
#         break

#     # print("condition6:", year % 4 == 0)
#     if year % 4 == 0:
#         leap_year = year + 4
#         break

# print(f"The next leap year after {year} is {leap_year}")
    