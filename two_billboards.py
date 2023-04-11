import sys
#imports system

sys.stdin = open("billboard.in")
#opens file
sys.stdout = open("billboard.out", "w")
#redirects file

board = []
board1 = []
board2 = []
a, b, c, d = map(int, input().split())
#inputs values for first billboard
e, f, g, h = map(int, input().split())
#inputs values for second billboard
i, j, k, l = map(int, input().split())
#inputs values for truck

board = [a,b,c,d]
board1 = [e,f,g,h]
board2 = [i,j,k,l]

# blocked billboard USACO problem

def area(board):
    return (board[2] - board[0]) * (board[3] - board[1])


def overlap(board1, board2):
    xbottom =max(board1[0], board2[0])
    xtop = min(board1[2], board2[2])

    yleft = max(board1[1], board2[1])
    yright = min(board1[3], board2[3])

    delta_x = xtop - xbottom
    delta_y = yright - yleft

    return delta_x * delta_y if delta_x > 0 and delta_y > 0 else 0
 

# first_board = (1,2,3,5)
# second_board = (6, 0, 10, 4)
# third_board = (2, 1, 8, 3)

print(area(board) - overlap(board, board2) + area(board1) - overlap(board1, board2))