# usaco input lines - testing
import sys
n_observations = int(input())
observations = []
for idx in range(n_observations):
    cow, side = map(int, input().split())
    observations.append((cow, side))

# comment below 2 lines for USACO
# n_observations=8
# cow_road_side = [[3,1],[3,0],[6,0],[2,1],[4,1],[3,0],[4,0],[3,1]] 

num_crosses = 0
cow_to_last_side_seen = {}

for observation in observations:
    cow, side = observation
    if cow in cow_to_last_side_seen:
        last_side = cow_to_last_side_seen[cow]
        if last_side != side:
            num_crosses += 1

    cow_to_last_side_seen[cow] = side

print(num_crosses)
