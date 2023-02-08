import numpy as np

#buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[2,4,7],[2,9,10],[2,10,8],[3,7,15],[5,12,12],[15,20,10],[19,24,8],[2,5,12]]
#buildings = [[0,2,3],[2,5,3]]

np_buildings = np.array(buildings)

print(np_buildings)

# print("After sorting on last axis: ")
# print(np.sort(np_buildings))

# print("After sorting on axis = 0: ")
# print(np.sort(np_buildings, axis=0))

# print("After arg-sorting on axis = -1: ")
# print(np_buildings[np_buildings[:,-1].argsort()])
#print(np_buildings[np_buildings[:,1].argsort()[::-1]])
# print(np_buildings[np.argsort(np_buildings)[::1,0]])

# LEXSORT - sort using multiple column-criteria
# the last in the sort-order is "primary" and so on going reverse
#  syntax: k[np.lexsort((k[:,2], k[:,1], k[:,0]))]
print("After lexsorting")
np_buildings = np_buildings[np.lexsort([-np_buildings[:,2], np_buildings[:,0]])]
# print(np_buildings[np.lexsort([-np_buildings[:,2], np_buildings[:,0]])])
print(np_buildings)

# LOOP through array
# print("shape[0] is: ", np_buildings.shape[0])
for x in reversed(range(np_buildings.shape[0])):
    print(x," : ")
    #if(np_buildings[0,x]==np_buildings[0,x-1]) and x>0:
    # if(np.np_buildings([0,x])==np.np_buildings([0,x-1])) and x>0:
    # print(np_buildings[0,x])


# INSERT row/s
# syntax: newArr = np.insert(arr, 2, (99, 99, 99), axis=0)
np_buildings = np.insert(np_buildings,2,(99,99,99), axis=0)
print("After inserting values:")
print(np_buildings)


# print("After sorting: ")
# print(np_buildings)
print("shape is", np.shape(np_buildings))
# print("The second row is", np_buildings[1,:])
print("dimension is", np.ndim(np_buildings))
print("minimum value is", np.min(np_buildings))
print("sum of each row is", np.sum(np_buildings, axis=0))

# np_buildings_2 = np.copy(np_buildings)
# np_buildings_2 = sorted(np_buildings, key=lambda row: (row[0], -row[2]))

# np_buildings_2 = np_buildings[np_buildings[[:,0],[:,-2]].argsort()]

# np_buildings_2[0,1] = 99
# print("np2 is sorted across 2 columns, 2nd column is descending:")
# print(np_buildings_2)
# print(np_buildings==np_buildings_2)
list_np = np_buildings.tolist()
print("this is list_np", list_np)

# list_np_2 = np_buildings_2.tolist()
# print("this is list_np", list_np_2)