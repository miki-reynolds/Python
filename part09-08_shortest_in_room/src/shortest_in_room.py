class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if len(self.people) == 0:
            return True
        else:
            return False

    def shortest(self):
        p = Person("",0)
        if len(self.people) > 0:
            for person in self.people:
                if p.height == 0 or person.height < p.height:
                    p = person
                    p.name = person.name
                    p.height = person.height
            return p

        else:
            return None

    def remove_shortest(self):
        minH = 0
        minP = ""
        i = 0
        if len(self.people) > 0:
            for num, person in enumerate(self.people):
                if minH == 0 or person.height < minH:
                    minP = person.name
                    minH = person.height
                    i = num
            removed = self.people.pop(i)
            return removed
        else:
            return None


    def print_contents(self):
        if len(self.people) > 0:
            sum = 0
            for person in self.people:
                sum += person.height

            print(f"There are {len(self.people)} persons in the room, and their combined height is {sum} cm")
            
            for person in self.people:
                print(person)
        else:
            return None

# room = Room()

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))

# print()

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# print()

# room.print_contents()