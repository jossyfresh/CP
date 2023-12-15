from collections import defaultdict,deque
n = int(input())
adjlist = defaultdict(list)
indegree = defaultdict(int)
nodes = set()
for _ in range(n-1):
    x,y = map(int,input().split())
    nodes.add(x)
    nodes.add(y)
    adjlist[x].append(y)
    adjlist[y].append(x)
    indegree[x] += 1
    indegree[y] += 1
queue = deque()
visited = set()
for n in nodes:
    if indegree[n] == 1:
        queue.append(n)
level = 0
while queue:
    n = len(queue)
    while n:
        n -= 1
        cur = queue.popleft()
        for node in adjlist[cur]:
            indegree[node] -= 1
            if indegree[node] == 1:
                queue.append(node)
    level += 1
    if len(queue) == 1:
        level *= 2
        break
    if len(queue) == 0:
        level *= 2
        level -= 1
        break

print(max(level*3,0))