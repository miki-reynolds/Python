def fractionate(amount: int):
    from fractions import Fraction
    num = Fraction(1, amount)
    list = []
    for i in range(amount):
        list.append(num)
    return list
