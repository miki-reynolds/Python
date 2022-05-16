word = input("Word: ")
print("*" *30)
leng = 14 - (len(word)/2)
if len(word) %2 == 0:
    print("*" + " " *int(leng) + word + " " * int(leng) + "*")
else:
    print("*" + " " *int(leng) + word + " " * (int(leng)+1) + "*")
print("*" *30)
