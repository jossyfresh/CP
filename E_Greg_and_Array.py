n,m,k  = map(int,input().split())
nums = list(map(int,input().split()))
nums.append(0)
for _ in range(m):
    l,r,d = map(int,input().split())
    nums[l] += d
    nums[r] += d
s = 0
print(nums)
for i in range(len(nums)):
    nums[i] += s
    s += nums[i]
ans = []
print(nums)
for _ in range(k):
    x,y = map(int,input().split())
    val = nums[y] - nums[x]
    print(val)

