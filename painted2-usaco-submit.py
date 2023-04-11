# An extension of the blocked billboard problem
import sys
#imports system

sys.stdin = open("billboard.in")
#opens file
sys.stdout = open("billboard.out", "w")
#redirects file

first_board = []
second_board = []

a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

first_board = [a, b, c, d]
second_board = [e, f, g, h]

x1 = first_board[0]
y1 = first_board[1]
x2 = first_board[2]
y2 = first_board[3]
x3 = second_board[0]
y3 = second_board[1]
x4 = second_board[2]
y4 = second_board[3]

def area(board):
    return (board[2] - board[0]) * (board[3] - board[1])

def delta_x(board):
    return (board[2] - board[0])

def delta_y(board):
    return (board[3] - board[1])

def overlap(board1, board2):
    xbottom = max(board1[0], board2[0])
    xtop = min(board1[2], board2[2])

    yleft = max(board1[1], board2[1])
    yright = min(board1[3], board2[3])

    delta_x = xtop - xbottom
    delta_y = yright - yleft

    return delta_x * delta_y if delta_x > 0 and delta_y > 0 else 0

# L-board is within F-board
if(
    (x3 <= x1 <= x4 and x3 <= x2 <= x4) and
    (y3 <= y1 <= y4 and y3 <= y2 <= y4)
    ):
    print(0)

# L-board is wider and taller than F-board
elif(
    (x3 > x1 and x4 < x2) and
    (y3 > y1 and y4 < y2)    
    ):
    print(area(first_board))    

# no overlap
elif(
    x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3    
    ):
    print(area(first_board))  


# in x axis, L brd us narrower than F brd, but covers F brd and is taller than F Brd
# in y axis, L brd us narrower than F brd, but covers F brd and is taller than F Brd
elif(
    ((x3 <= x1 <= x4 and x3 <= x2 <= x4) and
    (y3 >= y1  and y4 <= y2))
    or
    ((y3 <= y1 < y4 and y3 < y2 <= y4) and
    (x3 >= x1  and x4 <= x2))
    ): 
    print(area(first_board))

# one side complete  overlap
elif(
    (x3 <= x1 <= x4 <= x2 and y3 <= y1 <= y2 <= y4) or
    (x1 <= x3 <= x2 <= x4 and y3 <= y1 <= y2 <= y4) or
    (y3 <= y1 <= y4 <= y2 and x3 <= x1 <= x2 <= x4) or
    (y1 <= y3 <= y2 <= y4 and x3 <= x1 <= x2 <= x4)    
    ):
    print(area(first_board)-overlap(first_board, second_board))  

else:
    (print(area(first_board)))

print("\n") 
