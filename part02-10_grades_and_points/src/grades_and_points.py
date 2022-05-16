grade = int(input("How many points [0-100]: "))
if 0 <= grade <= 49:
    print("fail") 
elif 50 <= grade <= 59:
    print("Grade: 1") 
elif 60 <= grade <= 69:
    print("Grade: 2") 
elif 70 <= grade <= 79:
    print("Grade: 3") 
elif 80 <= grade <= 89:
    print("Grade: 4") 
elif 90 <= grade <= 100:
    print("Grade: 5") 
else:
    print("impossible!")