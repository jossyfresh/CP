from collections import defaultdict,deque
t =  int(input())
for _ in range(t):
    n,m = map(int,input().split())
    adjlist= defaultdict(list)
    indegree = defaultdict(set)
    for _ in range(m):
        x,y = map(int,input().split())
        adjlist[x].append(y)
        adjlist[y].append(x)
        indegree[y].add(x)
        indegree[x].add(y)
    queue= deque()
    for x in indegree:
        if len(indegree[x]) == 1:
            queue.append(x)
    ans = []
    visited= set()
    while queue:
        n = len(queue)
        ans.append(n)
        while n:
            n -= 1
            cur = queue.popleft()
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    indegree[node].remove(cur)
                    if len(indegree[node]) == 1:
                        queue.append(node)
                        visited.add(node)
    print(f'{ans[1]} {ans[0]//ans[1]}')
