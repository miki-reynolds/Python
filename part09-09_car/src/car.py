class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        if self.__petrol == 0:
            self.__petrol += 60

    def drive(self, km: int):
        d = self.__petrol
        if 0 <= self.__petrol <= km:
            self.__odometer += d
            self.__petrol -= d
        else:
            self.__odometer += km
            self.__petrol -= km


    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

# car = Car()
# print(car)
# car.fill_up()
# print(car)
# car.drive(20)
# print(car)
# car.drive(50)
# print(car)
# car.drive(10)
# print(car)
# car.fill_up()
# car.fill_up()
# print(car)
