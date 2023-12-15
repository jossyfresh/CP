import heapq
from collections import defaultdict
n,m = map(int,input().split())
adjlist = defaultdict(list)
for _ in range(m):
    x,y,z = map(int,input().split())
    adjlist[x-1].append((y-1,z))
    adjlist[y-1].append((x-1,z))
distance = [float('inf') for i in range(n)]
parent = [float('inf') for i in range(n)]
distance[0] = 0
queue = [(0,0)]
visited = set()
while queue:
    curdist,curnode = heapq.heappop(queue)
    if curdist in visited:
        continue
    for node,wei in adjlist[curnode]:
        if distance[node] > wei + curdist:
            distance[node] = wei + curdist
            parent[node] = curnode
            heapq.heappush(queue,(distance[node],node))
cycles = []
index = n-1
flag = 1
while (True):
    if parent[index] == float("inf"):
        if index == 0:
            cycles.append(1)
        else:
            flag = 0
        break
    cycles.append(index+1)
    if index in visited:
        flag = 0
        break
    visited.add(index)
    index = parent[index]
cycles.reverse()
if flag:
    print(*cycles)
else:
    print(-1)

