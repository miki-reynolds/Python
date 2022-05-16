from random import*

def roll(die: str):
    if die == "A":
        lA = [3, 3, 3, 3, 3, 6]
        sel = choice(lA)

    if die == "B":
        lB = [2, 2, 2, 5, 5, 5]
        sel = choice(lB)

    if die == "C":
        lC = [1, 4, 4, 4, 4, 4]
        sel = choice(lC)

    return sel

def play(die1: str, die2: str, times: int):
    lA = [3, 3, 3, 3, 3, 6]
    lB = [2, 2, 2, 5, 5, 5]
    lC = [1, 4, 4, 4, 4, 4]
    d1_win = 0
    d2_win = 0
    tie = 0
    for i in range(times):
        d1 = roll(die1)
        d2 = roll(die2)
        if d1 > d2:
            d1_win += 1
        elif d1 < d2:
            d2_win += 1
        else:
            tie += 1
    
    return (d1_win, d2_win, tie)




    