class BankAccount:
    def __init__(self, name, num, bal):
        self.__name = name
        self.__acctN = num
        self.__bal = bal
    
    @property
    def balance(self):
        return self.__bal

    def deposit(self, amount):
        if amount > 0:
            self.__bal += amount
            self.__service_charge()
        else:
            raise ValueError

    def withdraw(self, amount):
        if amount > 0 and self.__bal >= amount:
            self.__bal -= amount
            self.__service_charge()
        else:
            raise ValueError

    def __service_charge(self):
        self.__bal *= 0.99
