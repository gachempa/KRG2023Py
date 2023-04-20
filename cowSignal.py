# usaco input lines

import sys
# sys.stdin = open("cowsignal.in", "r")
# sys.stdout = open("cowsignal.out", "w")

m, n, k = map(int, input().split())

mnk = [m,n,k]

#mnk = [1,4,2]

def amplify(nstring,a,b):
    nstring1=list(nstring*b)
    nstring2=nstring1.copy()
#    print(nstring1)
    for x in range(a):
        nstring2[2*x]=nstring1[x]
        nstring2[2*x+1]=nstring1[x]
#    print(nstring2)    
    nstring3 = ("".join(map(str,nstring2)))
    for x in range(b):
        print(nstring3)

for x in range(mnk[0]):
    n_string = input()
    amplify(n_string,mnk[1],mnk[2])
#    n_string = "XXX."
#    amplify(n_string,mnk[1],mnk[2])

