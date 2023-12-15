from collections import deque
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
queue = deque(nums)
ans = []
if queue and queue[-1] == 2:
    ans.append(2)
    queue.pop()
if queue and queue[0] == 1:
    ans.append(1)
    queue.popleft()
while queue:
    while queue and queue[-1] == 2:
        ans.append(2)
        queue.pop()
    while queue and queue[0] == 1:
        ans.append(1)
        queue.popleft()
x = 0
print(*ans)
