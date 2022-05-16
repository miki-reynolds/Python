class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents/100
        self.__sum = euros + cents/100
    
    @property
    def euros(self):
        return self.__euros

    @property
    def cents(self):
        return self.__cents

    def __repr__(self):
        return f"{self.__sum:.2f}"

    def __eq__(self, another):
        return repr(self) == repr(another)
        
    def __lt__(self, another):
        return repr(self) < repr(another)

    def __gt__(self, another):
        return repr(self) > repr(another)

    def __ne__(self, another):
        s1 = self.euros + self.cents
        s2 = another.euros + another.cents
        return s1 != s2

    def __add__(self, another):
        s1 = self.__sum
        s2 = another.__sum
        result = s1 + s2
        return f"{result:.2f} eur"

    def __sub__(self, another):
        s1 = self.euros + self.cents
        s2 = another.euros + another.cents
        result = s1 - s2

        if result >= 0:
            return f"{result:.2f} eur"
        else:
            raise ValueError(f"a negative result is not allowed")

    def __str__(self):
        return f"{self.__sum:.2f} eur"


