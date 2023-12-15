import sys
from collections import defaultdict
n = int(sys.stdin.readline())
dist = []
for _ in range(n):
    grid = list(map(int,sys.stdin.readline().split()))
    dist.append(grid)
k = int(sys.stdin.readline())
adjlist = []
res = []
adjlist = []
for _ in range(k):
    x,y,z = map(int,sys.stdin.readline().split())
    adjlist.append((x-1,y-1,z))
    dist[x-1][y-1] = min(dist[x-1][y-1],z)
    dist[y-1][x-1] = min(dist[y-1][x-1],z)
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][x-1] + dist[x-1][j])
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][y-1] + dist[y-1][j])
    visited = set()
    ans = 0
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited and (j,i) not in visited:
                ans += dist[i][j]
                visited.add((i,j))
    res.append(ans)
print(*res)