def older_people(people: list, year: int):
    list = []
    for person in people:
        if person[1] < year:
            list.append(person[0])
    return list