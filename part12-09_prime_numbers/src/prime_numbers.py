def prime_numbers():
    i is int
    while True:
        if i == 2:
            yield 2
        if i== 3:
            yield 3
        if i > 3:
            r = []
            for j in range(2, i-1):
                r.append(i%j)
            if not 0 in r:
                yield i
            
        i += 1



numbers = prime_numbers()
for i in range(8):
    print(next(numbers))