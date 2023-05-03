# usaco input lines - testing
# import sys

# n, m = map(int, input().split())

n = 3
m = 8

m_spottyGenome = []
m_plainGenome = []

bovine_genomes= ["AATCCCAT","GATTGCAA","GGTCGCAA","ACTCCCAG","ACTCGCAT","ACTTCCAT"]

# print(bovine_genomes[0][0])

for y in range(0,m):
    print("--------")
    for x in range(0, 2*n):
        if x<n:
            # print(bovine_genomes[x][y])
            # print("---")
            m_spottyGenome.append(bovine_genomes[x][y])
        if x>=n:
            m_plainGenome.append(bovine_genomes[x][y])

    print(m_spottyGenome)
    print(m_plainGenome)