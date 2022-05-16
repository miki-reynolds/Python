class Item:
    def __init__(self, name: str, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
   
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, maxw):
        self.__maxw = maxw
        self.__suit = []
        self.__sum = 0
    
    def add_item(self, new: Item):
        d = self.__maxw - self.__sum
        if d >= new.weight():
            self.__suit.append(new)
            self.__sum += new.weight()

    def print_items(self):
        for item in self.__suit:
            print(item)

    def weight(self):
        return self.__sum

    def heaviest_item(self):
        max = Item("", 0)
        for item in self.__suit:
            if item.weight() > max.weight():
                max = item
        return max

    def __str__(self):
        if len(self.__suit) == 1:
            return f"{len(self.__suit)} item ({self.__sum} kg)"
        else:
            return f"{len(self.__suit)} items ({self.__sum} kg)"


class CargoHold:
    def __init__(self, maxw):
        self.__cargo = []
        self.__maxw = maxw
        self.__sum = 0
        self.__d = self.__maxw - self.__sum
    
    def add_suitcase(self, new: Suitcase):
        if self.__d >= new.weight():
            self.__cargo.append(new)
            self.__sum += new.weight()
            self.__d -= new.weight()

    def print_items(self):
        for suitcase in self.__cargo:
            suitcase.print_items()

    def __str__(self):
        if len(self.__cargo) == 1:
            return f"1 suitcase, space for {self.__d} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.__d} kg"
    
