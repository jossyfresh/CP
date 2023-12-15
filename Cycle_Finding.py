import sys
from collections import defaultdict
n,k = map(int,sys.stdin.readline().rstrip().split())
adjlist = []
for _ in range(k):
    x,y,z = map(int,sys.stdin.readline().rstrip().split())
    adjlist.append([x-1,y-1,z])
dist = [0 for i in range(n)]
parent = [float('inf') for i in range(n)]
index = 0
cycle = False
for _ in range(n-1):
    for u, v, w in adjlist:
       if dist[u] != float("inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
for u, v, w in adjlist:
    if dist[u] != float("inf") and  dist[u] + w < dist[v]:
        index = v
        cycle = True
        break

if cycle:       
    cycles = []       
    visited = set()
    while (True):
        if index == float('inf'):
            cycles.append(1)
            break
        cycles.append(index+1)
        if index in visited:
            break
        visited.add(index)
        index = parent[index]
    cycles.reverse()
    print("YES")
    print(*cycles)
else:
    print("NO")