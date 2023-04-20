# usaco input lines - works
# import sys

# n,m = map(int, input().split())
# n_road_speed=[None]*n
# m_drive_speed=[None]*m

# for x in range(n):
#     a,b = map(int, input().split())
#     n_road_speed[x]=a,b
# for x in range(m):
#     a,b = map(int, input().split())
#     m_drive_speed[x]=a,b


n,m=3,3
n_road_speed = [[40,75],[50,35],[10,45]]
m_drive_speed = [[40,76],[20,30],[40,40]]

n_currentindex=0
m_currentindex=0
maxoverspeed=0
n_distcovered=0
m_distcovered=0

def calcoverspeed(speedm, speedn,currentmax):
    overspeed=speedm-speedn
    newmax=max(currentmax,overspeed)
    return(newmax)

for x in range(n+m):
    if x==0:
        n_distcovered=n_road_speed[0][0]
        m_distcovered=m_drive_speed[0][0]
        maxoverspeed=calcoverspeed(m_drive_speed[m_currentindex][1], n_road_speed[n_currentindex][1],maxoverspeed)        
    if n_distcovered==m_distcovered==100:
        break
    elif n_distcovered==m_distcovered:
        n_currentindex+=1
        m_currentindex+=1
        n_distcovered=n_distcovered+n_road_speed[n_currentindex][0]
        m_distcovered=m_distcovered+m_drive_speed[m_currentindex][0]
        maxoverspeed=calcoverspeed(m_drive_speed[m_currentindex][1], n_road_speed[n_currentindex][1],maxoverspeed)

    elif n_distcovered<m_distcovered:
        n_currentindex+=1
        n_distcovered=n_distcovered+n_road_speed[n_currentindex][0]
        maxoverspeed=calcoverspeed(m_drive_speed[m_currentindex][1], n_road_speed[n_currentindex][1],maxoverspeed)

    elif n_distcovered>m_distcovered:
        m_currentindex+=1
        m_distcovered=m_distcovered+m_drive_speed[m_currentindex][0]
        maxoverspeed=calcoverspeed(m_drive_speed[m_currentindex][1], n_road_speed[n_currentindex][1],maxoverspeed)

print(maxoverspeed)