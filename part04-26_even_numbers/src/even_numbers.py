def even_numbers(my_list):
    new_list = []
    for number in my_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list