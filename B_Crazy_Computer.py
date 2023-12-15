nums = list(map(int,input().split()))
p = int(input())
for i in range(len(nums)):
    nums[i] = (nums[i],i)
nums.sort()
vals = []
for i in range(len(nums)-1):
    vals.append((abs(nums[i][0]-nums[i+1][0]),nums[i][1],nums[i+1][1]))
visited = set()
vals.sort()
i = 0
while p:
    if vals[i][1] not in visited and vals[i][1]


