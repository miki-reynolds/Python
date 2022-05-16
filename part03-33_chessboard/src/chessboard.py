def chessboard(number):
  row = 1
  while row <= number:
    column = 1
    while column <= number:
      position = row + column
      if position % 2 == 0:
        print("1", end="")
      else:
        print("0", end="")
      column +=1
    print()
    row += 1
    
# Testing the function
if __name__ == "__main__":
    chessboard(3)
