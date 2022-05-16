
def print_sudoku(sudoku: list):
  for row in range(9):
    if row != 0:
      if(row % 3 == 0):
        print()
        print()

    for col in range(9):
      val = sudoku[row][col]
      if col != 0:
        if(col % 3 == 0):
            print(" ", end='')
      if(val == 0):
        print("_ ", end='')
      else:
        print(val, end=' ')
    print()

    # for i, row in enumerate(sudoku):
    # print(("{}{}{} " * 3).format(*[x if x != 0 else "_" for x in row]))
    # but there is line break after every 3 lines

def add_number(sudoku: list, row_no: int,  column_no: int, number: int):
    sudoku[row_no][column_no] = number
    return sudoku[row_no][column_no]

sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)