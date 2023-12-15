import heapq

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

avoid = [tuple(map(int, input().split())) for _ in range(k)]

dist = [float('inf')] * (n+1)
dist[1] = 0

heap = [(0, 1)]
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    
    for v in graph[u]:
        if (u, v, _) in avoid or (_, u, v) in avoid:
            continue
            
        new_dist = dist[u] + 1
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(heap, (new_dist, v))
            
if dist[n] == float('inf'):
  print(-1)
else:
  print(dist[n])
  
  path = [n]
  u = n
  while u != 1:
    for v in graph[u]:
      if dist[v] == dist[u] - 1:
        path.append(v)
        u = v
        break
          
path = [n]
u = n
while u != 1:
    for v in graph[u]:
        if dist[v] == dist[u] - 1:
            path.append(v)
            u = v
            break

print(*reversed(path))


