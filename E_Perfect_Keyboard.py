from collections import defaultdict,deque
n = int(input())
for _ in range(n):
    adjlist = defaultdict(set)
    x = input()
    for i in range(len(x)):
        if i == 0 and i+1 < len(x):
            adjlist[x[i]].add(x[i+1])
        elif i != 0 and i + 1 < len(x):
            adjlist[x[i]].add(x[i+1])
            adjlist[x[i]].add(x[i-1])
        else:
            adjlist[x[i]].add(x[i-1])
    visited = set()
    flag = [0]
    path = []
    def dfs(cur,par):
        visited.add(cur)
        for node in adjlist[cur]:
            if node not in visited:
                dfs(node,cur)
            elif node in visited and node != par:
                flag[0] = 1
        return
    dfs(x[0],-1)
    for x in adjlist:
        if len(adjlist[x]) > 2:
            flag[0] = 1
            break
    if flag[0]:
        print("NO")
    else:
        print("YES")
        vi = set()
        q = deque()
        l = 0
        r = 0
        while r < len(x):
            if x[r] not in vi:
                vi.add(x[r])
                q.append(x[r])
                r += 1    
            else:
                q.popleft()
        print(*q)

            


