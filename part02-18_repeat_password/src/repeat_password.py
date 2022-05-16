pass1 = input("Password: ")
while True:
    if input("Repeated password: ") == pass1:
        break
    print("They do not match!")
print("User account created!")