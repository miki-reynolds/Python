from datetime import datetime
def dob(pic: str):
    try:
        special = ""
        if pic[6] == "+":
            a = "18" + pic[4:6]
    
        if pic[6] == "-":
            a = "19" + pic[4:6]

        if pic[6] == "A":
            a = "20" + pic[4:6]

        b = pic[2:4]
        c = pic[:2]
        if pic[2] == "0":
            b = pic[3]
        if pic[0] == "0":
            c = pic[1]
        if datetime(int(a), int(b), int(c)):
            return True
    except:
        return False

# print(dob("290200A1239"))
# pic = "290200A1239"

# if pic[6] == "+":
#     a = "18" + pic[4:6]
    
# if pic[6] == "-":
#     a = "19" + pic[4:6]
    
# if pic[6] == "A":
#     a = "20" + pic[4:6]

# print(a)
# b = pic[2:4]
# c = pic[:2]
# if pic[2] == "0":
#     b = pic[3]
# if pic[0] == "0":
#     c = pic[1]
# dob = datetime(int(a), int(b), int(c))
# # print(dob)


def century(pic: str):
    if pic[6] == "-" or pic[6] == "+" or pic[6] == "A":
        return True
# print(century("290200A1239"))

def control(pic: str):
    list = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    num = pic[:10]
    if num[0] == 0:
        num = num[1:]
    num = int(num.replace(num[6], ""))
    val = num % 31
    return list[val] == pic[-1]

# print(control("290200A1239"))

def is_it_valid(pic: str):
    if len(pic) != 11:
        # print(len(pic))
        return False
    elif dob(pic) is False:
        # print(dob(pic))
        return False
    elif century(pic) is False:
        # print(century(pic))
        return False
    elif control(pic) is False:
        # print(control(pic))
        return False
    
    return True

# print(is_it_valid("290200A1239"))