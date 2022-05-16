import string

def run(list: list):
    var_list = string.ascii_uppercase
    location_list = string.ascii_lowercase + string.digits

    for cmmd in list:
        if cmmd[:5] == "PRINT":
            print()
        if cmmd[:3] == "MOV":
            cmmd[4] == int(cmmd[6:])

        if cmmd[:3] == "ADD":
            cmmd[4] += int(cmmd[6])

        if cmmd[:3] == "SUB":
            cmmd[4] -= int(cmmd[6])

        if cmmd[:3] == "MUL":
            cmmd[4] *= int(cmmd[6])

        if cmmd[:3] == "JUMP":
            cmmd[4] == int(cmmd[6])
            

