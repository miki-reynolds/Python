while True:
    question = input("Editor: ").lower()
    if question == "Visual Studio Code":
        print("an excellent choice!")
        break
    elif question == "Word" or question =="Notepad":
        print("awful")
    else:
        print("not good")