class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers

    def add_number(self, num):
        self.__numbers.append(num)

    def address(self):
        return self.__address

    def add_address(self, addr):
        self.__address = addr


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
    
        self.__persons[name].add_number(number)
    
    def add_address(self, name, address):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
    
        self.__persons[name].add_address(address)

    def get_entry(self, name):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        entry = self.__phonebook.get_entry(name)

        if self.__phonebook.get_entry(name) == None:
            print("number unknown") 
            print("address unknown") 
            
        elif self.__phonebook.get_entry(name) != None:
            if entry.numbers() == []:
                print("number unknown")
            if entry.numbers() != []:
                for num in entry.numbers():
                    print(num)

            if entry.address() == None:
                print("address unknown") 
            if entry.address() != None:
                print(entry.address())


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

    

# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# phonebook.add_address("Eric", "Viherlaaksontie 7, Espoo")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("E"))