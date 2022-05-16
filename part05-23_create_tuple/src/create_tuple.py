def create_tuple(x: int, y: int, z: int):
    list = [x, y, z]
    tuple = (min(list), max(list), x+y+z)
    return tuple