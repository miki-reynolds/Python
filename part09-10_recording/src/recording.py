class Recording:
    def __init__(self, num: int):
        if num >= 0:
            self.__length = num
        else:
            raise ValueError("cant be below zero")

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, num: int):
        if num >= 0:
            self.__length = num
        else:
            raise ValueError
    

the_wall = Recording(43)
print(the_wall)
the_wall.length = 44
print(the_wall.length)