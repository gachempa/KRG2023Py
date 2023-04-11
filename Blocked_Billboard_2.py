import sys
sys.stdin = open("billboard.in")
sys.stdout = open("billboard.out", "w")

board = []
board1 = []
a, b, c, d = map(int, input().split())
#inputs values for lawnmower billboard
e, f, g, h = map(int, input().split())
#inputs values for cowfeed billboard

board = [a,b,c,d]
#LAWNMOWER
board1 = [e,f,g,h]
#COWFEED

# if board1[0] <= board[0] or board[2] <= board1[2] and board1[1] <= board[1] or board[3] <= board[3] == False:
#     print(board[2]-board[0])*(board[3]-board[1])
# #if the two boards are not connecting

if (
    ((board1[0]<= board[0] <= board1[2] and board1[0] <= board[2] <= board1[2]) and
     


    

def area(board1):
    return (board1[2] - board1[0]) * (board1[3] - board1[1])


def overlap(board1, board):
    xbottom =max(board1[0], board[0])
    xtop = min(board1[2], board[2])

    yleft = max(board1[1], board[1])
    yright = min(board1[3], board[3])

    delta_x = xtop - xbottom
    delta_y = yright - yleft

    return delta_x * delta_y if delta_x > 0 and delta_y > 0 else 0

if 
