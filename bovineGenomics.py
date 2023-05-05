# usaco input lines - testing
# import sys
# n, m = map(int, input().split())
# bovine_genomes= []
# for x in range(0,2*n):
#     bovine_genomes.append(input())

# comment below 3 lines for USACO
n = 3
m = 8
bovine_genomes= ["AATCCCAT","GATTGCAA","GGTCGCAA","ACTCCCAG","ACTCGCAT","ACTTCCAT"]

m_spottyGenome = []
m_plainGenome = []
locationscore = 0

def mutation(listspotty, listplain, ncows, n_position):
    matches = ncows
    for x in range(0, ncows):
        if listspotty[x] not in listplain:
            matches = matches - 1
    if matches == 0: 
        # comment below line for USACO
        print("position with no genome match: ", n_position, listspotty, listplain)
        return 1
    else: return 0

for y in range(0,m):
    m_spottyGenome.clear()
    m_plainGenome.clear()       
    for x in range(0, n):
        m_spottyGenome.append(bovine_genomes[x][y])
        m_plainGenome.append(bovine_genomes[n+x][y])
        if x == n-1:
            locationscore = locationscore + mutation(m_spottyGenome, m_plainGenome, n, x)

print(locationscore)