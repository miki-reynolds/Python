def distinct_numbers(list):
    new = []
    for number in list:
        if number not in new:
            new.append(number)
    new.sort()
    return new
