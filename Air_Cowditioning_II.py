cows_list = []
#list tracking cow's starting starting and ending stall, and by how degrees their stall need to be cooler
ac_list = []
#list tracking 
n = int(input()); m = int(input())
for i in range (0,n):
   input_1 = input().split()
   cows_list.append(input_1)
print(cows_list)
for i in range (0,m):
   input_1 = input().split()
   ac_list.append(input_1)
print(ac_list)


