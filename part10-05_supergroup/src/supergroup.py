class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'


class SuperGroup:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._members = []
    
    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def add_member(self, mem: SuperHero):
        self._members.append(mem)
    
    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for member in self._members:
            print(member)
