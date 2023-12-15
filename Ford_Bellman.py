import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
adjlist = []
for _ in range(k):
    x,y,z = map(int,sys.stdin.readline().rstrip().split())
    adjlist.append([x-1,y-1,z])

dist = [30000 for i in range(n)]
dist[0] = 0
for _ in range(n-1):
    for u, v, w in adjlist:
       if dist[u] != float("inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
print(*dist)