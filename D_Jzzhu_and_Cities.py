import heapq,sys
from collections import defaultdict
n,m,k = map(int,sys.stdin.readline().split())
adjlist = defaultdict(list)
def dijkstra(graph):
    distances = [float('inf') for i in range(n+1)]
    distances[1] = 0
    visited = set()
    ans = 0
    heap = [(0,1,False)]
    while heap:
        current_distance, current_node,train = heapq.heappop(heap)
        if current_node not in visited:
            visited.add(current_node)
            for weight, neighbor,istrain in graph[current_node]:
                distance = current_distance + weight
                if distance <= distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor,istrain))
                else:
                    if istrain:
                        ans += 1
        elif train:
            ans += 1
    return ans
for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    adjlist[x].append((z,y,False))
    adjlist[y].append((z,x,False))
vist = {}
skip = 0
for _ in range(k):
    x,z = map(int,sys.stdin.readline().split())
    if x in vist:
        vist[x] = min(vist[x],z)
        skip += 1
    else:
        vist[x] = z
for x in vist:
    adjlist[1].append((vist[x],x,True))
res = dijkstra(adjlist)
print(skip + res)


