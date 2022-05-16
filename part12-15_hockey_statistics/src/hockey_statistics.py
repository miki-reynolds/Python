import json
file = input("file name: ")
print("read the data of 14 players")
print('''
commands:

0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

''')
with open(file, "r") as f:
    r = json.load(f)
    print(f"read the data of {len(r)} players")

scores = [(i["goals"] + i["assists"]) for i in r]
for n in range(0, len(r)):
    r[n]["scores"] = scores[n]

while True:
    cmd = int(input("command: "))
    if cmd == 0:
        break

    elif cmd == 1:
        name_f = input("name: ")
        for i in r:
            name = i["name"]
            team = i["team"]
            assis = i["assists"]
            goals = i["goals"]
            ttl = assis + goals
            if name == name_f:
                print(f"{name:20} {team} {goals:3} + {assis:2} = {ttl:3}")
               
    elif cmd == 2:
        teams = sorted(list(set(map(lambda x: x["team"], r))))
        for i in teams:
            print(i)

    elif cmd == 3:
        result = sorted(list(set(map(lambda x: x["nationality"], r))))
        for i in result:
            print(i)
    
    elif cmd == 4:
        team_f = input("team: ")
        result = sorted(list(filter(lambda x: x["team"] == team_f, r)), key=lambda x: x["name"])
        for i in result:
            name = i["name"]
            team = i["team"]
            assis = i["assists"]
            goals = i["goals"]
            ttl = assis + goals
            if team == team_f:
                print(f"{name:20} {team} {goals:3} + {assis:2} = {ttl:3}")

    elif cmd == 5:
        country = input("country: ")
        result = sorted(list(filter(lambda x: x["nationality"] == country, r)), key=lambda x: x["scores"], reverse=True)
        for i in result:
            name = i["name"]
            team = i["team"]
            assis = i["assists"]
            goals = i["goals"]
            ttl = assis + goals
            # if i["nationality"] == country:
            print(f"{name:20} {team} {goals:3} + {assis:2} = {ttl:3}")

    elif cmd == 6:
        num = int(input("how many: "))
        scores = [(i["goals"] + i["assists"]) for i in r]

        for n in range(0, len(r)):
            r[n]["scores"] = scores[n]

        result = sorted(r, key=lambda x: (x["scores"], x["goals"]), reverse=True)
        for i in result[:num]:
            name = i["name"]
            team = i["team"]
            assis = i["assists"]
            goals = i["goals"]
            scores = i["scores"]
            print(f"{name:20} {team} {goals:3} + {assis:2} = {scores:3}")


    elif cmd == 7:
        num = int(input("how many: "))
        scores = [(i["goals"] + i["assists"]) for i in r]

        result = sorted(r, key=lambda x: (x["goals"], x["games"]*-1), reverse=True)
        for i in result[:num]:
            name = i["name"]
            team = i["team"]
            assis = i["assists"]
            goals = i["goals"]
            scores = assis + goals
            print(f"{name:20} {team} {goals:3} + {assis:2} = {scores:3}")





# test = [(5, 6, 13), (5, 7, 10), (6, 3, 1), (6, 4, 15)]
# r = sorted(test, key=lambda x: (x[0], x[1]), reverse=True)
# print(r)
# # while i+1 < len(r):
# #     for i in range(len(r)):
# #         if r[i][0] == r[i+1][0]:
# #             temp = r[i]


# k = sorted(r, key=lambda x: x[1], reverse=True)
# print(k)