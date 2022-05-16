print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum1 = 0
posi = 0
neg = 0
while True:
    num = int(input("Number: "))
    count += 1 
    # if count is put after num == 0. it wont count 0 as 1 count, bc it alreak breaks!!
    sum1 += num
    if num > 0:
        posi += 1
    elif num < 0:
        neg += 1
    else:
        count = count - 1
        break

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum1}")
print(f"The mean of the numbers is {sum1/count}")
print(f"Positive numbers {posi}")
print(f"Negative numbers {neg}")


    