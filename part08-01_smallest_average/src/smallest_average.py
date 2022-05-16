def average(person: dict):
    total = 0
    for key, value in person.items():
        if key != "name":
            total += person[key]
    return (total/3)

def smallest_average(person1: dict, person2: dict, person3: dict):
    ave1 = average(person1)
    ave2 = average(person2)
    ave3 = average(person3)
    list = [ave1, ave2, ave3]
    
    if min(list) == ave1:
        return person1
    if min(list) == ave2:
        return person2
    if min(list) == ave3:
        return person3

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))
