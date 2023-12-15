from collections import defaultdict
from collections import deque
n,m = map(int,input().split())
c = list(map(int,input().split()))
adjlist = defaultdict(list)
for _ in range(m):
    x,y = map(int,input().split())
    adjlist[x].append(y)
    adjlist[y].append(x)
visited = set()
val = 0
queue = deque()
for x in range(1,n+1):
    if x not in visited:
        queue.append(x)
        ans = c[x-1]
        while queue:
            cur = queue.popleft()
            ans = min(ans,c[cur-1])
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
        val += ans
print(val)
