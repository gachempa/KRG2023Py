import numpy as np

#buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[2,9,10],[2,10,8],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#buildings = [[0,2,3],[2,5,3]]

np_buildings = np.array(buildings)

print(np_buildings)

print("After sorting on last axis: ")
print(np.sort(np_buildings))

print("After sorting on axis = 0: ")
print(np.sort(np_buildings, axis=0))

print("After sorting: ")
print(np_buildings)
print("shape is", np.shape(np_buildings))
print("The second row is", np_buildings[1,:])
print("dimension is", np.ndim(np_buildings))
print("minimum value is", np.min(np_buildings))
print("sum of each row is", np.sum(np_buildings, axis=0))
