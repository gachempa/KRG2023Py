# An extension of the blocked billboard problem


#first_board = (2, 1, 7, 4) #lawnmower baord
second_board = (5, -1, 10, 3) # feed board
first_board = (4, 1, 11, 3) #lawnmower baord, test case 7

x1 = first_board[0]
y1 = first_board[1]
x2 = first_board[2]
y2 = first_board[3]
x3 = second_board[0]
y3 = second_board[1]
x4 = second_board[2]
y4 = second_board[3]

print(y3)

def area(board):
    return (board[2] - board[0]) * (board[3] - board[1])

def delta_x(board):
    return (board[2] - board[0])

def delta_y(board):
    return (board[3] - board[1])

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
