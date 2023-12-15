import heapq
n,k = map(int,input().split())
nums = []
for i in range(n):
    x,y = map(int,input().split())
    nums.append([y,x])
nums.sort(reverse=True)
x = 0
ans = []
heapq.heapify(ans)
total = 0

i = 0
for i in range(len(nums)):
    x += nums[i][1]
    heapq.heappush(ans,nums[i][1])
    if len(ans) > k:
        x -= heapq.heappop(ans)
    total = max(total,x * nums[i][0])
print(total)