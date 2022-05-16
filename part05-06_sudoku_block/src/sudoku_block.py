def block_correct(sudoku: list, row_no: int, column_no: int):
    point1 = sudoku[row_no][column_no]
    point2 = sudoku[row_no][column_no+1]
    point3 = sudoku[row_no][column_no+2]
    point4 = sudoku[row_no+1][column_no]
    point5 = sudoku[row_no+1][column_no+1]
    point6 = sudoku[row_no+1][column_no+2]
    point7 = sudoku[row_no+2][column_no]
    point8 = sudoku[row_no+2][column_no+1]
    point9 = sudoku[row_no+2][column_no+2]
   
    list = []
    list.append(point1)
    list.append(point2)
    list.append(point3)
    list.append(point4)
    list.append(point5)
    list.append(point6)
    list.append(point7)
    list.append(point8)
    list.append(point9)

    for point in list:
        if point > 0:
            if list.count(point) != 1:
                return False
    return True




 # new_list = [sudoku[row_no][column_no]:sudoku[row_no+2][column_no+2]]
    # list_check = []
    # for row in new_list:
    #     for cell in row:
    #         if cell > 0 and cell in list_check:
    #             return False
    #         list_check.append(cell)   
    # return True
