def times_ten(start_index: int, end_index: int):
    dict = {}
    for i in range(start_index, end_index+1):
        dict[i] = i*10
    return dict