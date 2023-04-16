# usaco input lines

# import sys
# sys.stdin = open("mixmilk.in")
# sys.stdout = open("mixmilk.out", "w")

# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())

# inputs_list = [[a,b],[c,d],[e,f]]


buckets = [[10,3],[11,4],[12,5]]

def pour(bucket1, bucket2):
    milk1 = bucket1[1]
    empty2 = bucket2[0]-bucket2[1]
    if milk1<=empty2:
        milk2=bucket2[1]+milk1
        milk1=0
    elif milk1>empty2:
        milk2=bucket2[0]
        milk1=milk1-empty2
    return(milk1,milk2)

for x in range(100):
    if x==0 or x%3==0:
        milka, milkb = pour(buckets[0],buckets[1])
        buckets[0][1]=milka
        buckets[1][1]=milkb
    elif x==1 or x%3==1:
        milka, milkb = pour(buckets[1],buckets[2])
        buckets[1][1]=milka
        buckets[2][1]=milkb
    elif x==2 or x%3==2:
        milka, milkb = pour(buckets[2],buckets[0])
        buckets[2][1]=milka
        buckets[0][1]=milkb

print(buckets[0][1])
print(buckets[1][1])
print(buckets[2][1])

print("\n")