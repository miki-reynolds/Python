list = []
print("The list is now []")

# 'd', 'r', 'd', 'd', 'd', 'r', 'r', 'x')
i = 1
while True:
    command = input("a(d)d, (r)emove or e(x)it: ").lower()

    if command == "r":
        list.pop()
        print("The list is now ", end='')
        i -=1
        print(list)    

    if command == "d":
        list.append(i)
        print("The list is now ", end='')
        print(list)
        i +=1
 
    if command == "x":
        print("Bye!")
        break


    