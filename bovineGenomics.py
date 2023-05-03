# usaco input lines - testing
# import sys

# n, m = map(int, input().split())

n = 3
m = 8

m_spottyGenome = []
m_plainGenome = []
locationscore = 0
bovine_genomes= ["AATCCCAT","GATTGCAA","GGTCGCAA","ACTCCCAG","ACTCGCAT","ACTTCCAT"]

def mutation(listspotty, listplain, ncows):
    i=0
    for x in range(0, ncows):
        if listspotty[x] in listplain:
            print("xxxx")
            print(listspotty[x])
            print("xxxx")
            break
        
        else: i = 1
    return i

for y in range(0,m):
    m_spottyGenome.clear()
    m_plainGenome.clear()       
    for x in range(0, n):
        m_spottyGenome.append(bovine_genomes[x][y])
        m_plainGenome.append(bovine_genomes[n+x][y])
        locationscore = locationscore + mutation(m_spottyGenome, m_plainGenome, n)

    print(m_spottyGenome)
    print(m_plainGenome)
print(locationscore)