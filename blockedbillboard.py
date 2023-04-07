# blocked billboard USACO problem

def area(board):
    return (board[2] - board[0]) * (board[3] - board[1])


def overlap(board1, board2):
    xbottom = max(board1[0], board2[0])
    xtop = min(board1[2], board2[2])

    yleft = max(board1[1], board2[1])
    yright = min(board1[3], board2[3])

    delta_x = xtop - xbottom
    delta_y = yright - yleft

    return delta_x * delta_y if delta_x > 0 and delta_y > 0 else 0


first_board = (1,2,3,5)
second_board = (6, 0, 10, 4)
third_board = (2, 1, 8, 3)

print(area(first_board) - overlap(first_board, third_board) + area(second_board) - overlap(second_board, third_board))
