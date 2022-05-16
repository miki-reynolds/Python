class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(em: Employee):
    count = len(em.subordinates)
    if count == 0:
        return 0
    else:
        for i in em.subordinates:
            count += count_subordinates(i)

    return count
