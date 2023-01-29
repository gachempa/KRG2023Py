nums = [2,7,11,15]
target = 26

a = 0
b = 0

len_nums = len(nums)

for x in range(0,len_nums):
    a = nums[x]
    for y in range(x,len_nums):
        b = nums[y]
        if a + b == target:
            print(x,y)

