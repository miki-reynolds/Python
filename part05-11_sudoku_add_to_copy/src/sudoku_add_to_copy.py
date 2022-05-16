def print_sudoku(sudoku: list):
  for row in range(9):
    if(row % 3 == 0):
      print()
      print()
    for col in range(9):
      val = sudoku[row][col]
      if(col % 3 == 0):
        print(end=' ')
      if(val == 0):
        print("_", end=' ')
      else:
        print(val, end=' ')
    print()
  
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  dub = sudoku[:]
  dub[row_no][column_no] = number
  return dub


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
grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)

