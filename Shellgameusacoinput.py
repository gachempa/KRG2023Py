
import sys
sys.stdin = open("shell.in")
sys.stdout = open("shell.out", "w")

n_swaps = map(int, input())
swaps=[]

for x in range (n_swaps):
  a, b, c = map(int, input().split())
  swaps[x] = a,b,c

position_abc = [[1,0,0],[0,1,0], [0,0,1]] 

score_a = 0
score_b = 0
score_c = 0

def doswap(a,b):
#    print(position_abc)
    x=position_abc[0][a-1]
    y=position_abc[1][a-1]
    z=position_abc[2][a-1]    
    position_abc[0][a-1]=position_abc[0][b-1]
    position_abc[0][b-1]=x

    position_abc[1][a-1]=position_abc[1][b-1]
    position_abc[1][b-1]=y

    position_abc[2][a-1]=position_abc[2][b-1]
    position_abc[2][b-1]=z

for x in range(n_swaps):
    var_x = swaps[x][0]
    var_y = swaps[x][1]
    choice = swaps[x][2]    

    doswap(var_x,var_y)

    if position_abc[0][choice-1] == 1: score_a += 1
    if position_abc[1][choice-1] == 1: score_b += 1
    if position_abc[2][choice-1] == 1: score_c += 1

print(max(score_a, score_b,score_c)) 

print("\n") 
