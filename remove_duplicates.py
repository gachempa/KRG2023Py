print("hello")
nums = [0,0,1,1,1,2,2,3,3,4]
x = nums[0]
y = 0
z = len(nums)
for i in range (0,z):
    if nums[i] != x:
        nums[y+1] = nums[i]
        y += 1
        x = nums[i]
        print(y)
        print(x)
        print(i)
        print(nums)
print(nums)
# nums[1] =  1
# print (nums)
# nums[2] = 2
# print (nums)
# nums[3] = 3
# print (nums)
# nums[4] = 4
# print (nums)
