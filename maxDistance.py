
# usaco input lines - works
# import sys

n = int(input(""))
n_x = [int(x) for x in input().split()]
n_y = [int(x) for x in input().split()]

maxdistance = 0

for x in range(n-1):
    for y in range(x+1,n):
        distxsq=(n_x[y]-n_x[x])**2
        distysq=(n_y[y]-n_y[x])**2
        distsq=distxsq+distysq
        maxdistance=max(maxdistance,distsq)
        
print(maxdistance)