from collections import defaultdict
from collections import deque,Counter
t = int(input())
for _ in range(t):
    empty = input()
    v,k = map(int,input().split())
    adjlist = defaultdict(list)
    indegree = defaultdict(int)
    for i in range(v-1):
        x,y = map(int,input().split())
        adjlist[x].append(y)
        adjlist[y].append(x)
        indegree[x] += 1
        indegree[y] += 1
    queue = deque()
    visited = set()
    for i in range(1,v+1):
        if indegree[i] == 1 or indegree[i] == 0:
            queue.append(i)
            visited.add(i)
    ans = 0
    while queue and k > 0:
        n = len(queue)
        ans += n
        while n:
            n -= 1
            cur = queue.popleft()
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    indegree[node] -= 1
                    if indegree[node] == 1:
                        queue.append(node)
                        visited.add(node)
        k -= 1
    print(v-ans)
    

