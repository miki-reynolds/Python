class SimpleDate:
    def __init__(self, d, m, y):
        self.__d = d
        self.__m = m
        self.__y = y

    def __value(self):
        return self.__y * 360 + self.__m * 30 + self.__d

    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
    def __str__(self):
        return f"{self.__d}.{self.__m}.{self.__y}"

    def __add__(self, num):
        original = self.__value()
        total = original + num

        y = total // 360
        m = (total % 360) // 30
        d = (total % 360) % 30
        result = SimpleDate(d,m,y)
        
        return result
      
    def __sub__(self, date: "SimpleDate"):
        original = self.__value()
        new = date.__value()
        
        result = abs(original - new)
        return result



