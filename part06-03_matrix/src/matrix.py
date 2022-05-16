def matrix():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            parts = [int(number) for number in parts]
            matrix.append(parts)
    return matrix

def row_sums():
    matrix()
    sums = []
    for row in matrix():
        sub = sum(row)
        sums.append(sub)
    return sums

def matrix_sum():
    return sum(row_sums())

def matrix_max():
    biggest = 0
    for row in matrix():
        if biggest == 0 or max(row) > biggest:
            biggest = max(row)
    return biggest

# print(matrix())
# print(matrix_max())
# print(matrix_sum())
# print(row_sums())

