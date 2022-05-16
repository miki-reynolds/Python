def factorials(n: int):
    dict = {}
    output = 1
    for i in range(1, n+1):
        dict[i] = i*output
        output *= i
    return dict