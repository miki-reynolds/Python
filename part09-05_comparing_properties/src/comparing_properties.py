class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: "RealProperty"):
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False
    
    def price_difference(self, compared_to:"RealProperty"):
        i1 = self.square_metres * self.price_per_sqm
        i2 = compared_to.square_metres * compared_to.price_per_sqm

        return abs(i1-i2)

    def more_expensive(self, compared_to:"RealProperty"):
        i1 = self.square_metres * self.price_per_sqm
        i2 = compared_to.square_metres * compared_to.price_per_sqm

        if i1 - i2 > 0:
            return True
        else:
            return False
            