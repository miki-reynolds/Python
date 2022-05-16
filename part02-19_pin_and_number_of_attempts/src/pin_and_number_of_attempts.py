pass1 = "4321"
attempts = 0
while True:
    pass2 = input("PIN: ")
    attempts += 1
    
    if pass2 == pass1:
        break
    
    print("Wrong")

if attempts == 1:
    print(f"Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
