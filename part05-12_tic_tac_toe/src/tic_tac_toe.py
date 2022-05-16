def play_turn(game_board: list, x: int, y: int, piece: str):
    if y < len(game_board) and x < len(game_board):
        if game_board[y][x] != "":
            return False
        else:
            game_board[y][x] = piece
            return True
    else:
        return False
       
