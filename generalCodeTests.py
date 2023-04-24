# usaco input lines - testing
import sys

#usaco daisy chains problem code snippets

n = int(input())
n_petals = [int(x) for x in input().split()]

# n = 4
# n_petals=[1,1,2,3]
n_average=0
flowers=[]

def naverage(alist):
#    print(alist)
    listavg=sum(alist) / len(alist)
    if listavg.is_integer and listavg in alist:
        return(1)
    else:
        return(0) 

for x in range(1, n+1):
#    print("x: ", x)
    for y in range(x, n+1):
        flowers.append(y)
        n_average = n_average + naverage(flowers)
        if y==n:
            flowers.clear()

print(n_average)