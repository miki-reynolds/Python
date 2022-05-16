def row_correct(sudoku: list, row_no: int):
    for cell in sudoku[row_no]:
        if cell > 0 and sudoku[row_no].count(cell) != 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    list = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in list:
            return False
        list.append(number)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    list = []
    for row in range(row_no, row_no +3):
        for col in range(column_no, column_no +3):
            number = sudoku[row][col]
            if number > 0 and number in list:
                return False
            list.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(9):
        if not row_correct(sudoku, row):
            return False
    
    for col in range(9):
        if not column_correct(sudoku, col):
            return False
    
    for row in range(9):
        for col in range(9):
            if col % 3 == 0 and row % 3 ==0:
                if not block_correct(sudoku, row, col):
                    return False

    return True

# sudoku1 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku1))

    
