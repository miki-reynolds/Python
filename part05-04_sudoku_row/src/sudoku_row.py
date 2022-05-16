def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for cell in row:
        if cell > 0 and row.count(cell) != 1:
            return False
    return True
       

# SudokuRowTest: test_3_functionality
# False != True : The result False is incorrect when calling
# sudoku = [
#   [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
#   [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],   # rivi 1
#   [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],   # rivi 2
#   [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
#   [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
#   [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
#   [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],   # rivi 6
#   [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
#   [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],   # rivi 8
# ]
# row_correct(sudoku, 4)