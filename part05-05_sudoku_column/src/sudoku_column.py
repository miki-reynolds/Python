
def column_correct(sudoku: list, column_no: int):
    col = []
    for row in sudoku:
        col.append(row[column_no])

    for cell in col:
        if cell > 0:
            if col.count(cell) != 1:
                return False
    return True


# def column_correct(sudoku: list, column_no: int):
#     list = []
#     for row in sudoku:
#         number = row[column_no]
#         if number > 0 and number in list:
#             return False
#         list.append(number)
#     return True

    