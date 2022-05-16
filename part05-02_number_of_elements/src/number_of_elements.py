def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for col in row:
            if col == element:
                count += 1
    return count