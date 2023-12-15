from collections import defaultdict,deque
n = int(input())
adjlist = defaultdict(list)
indegree = defaultdict(int)
nodes = set()
par = [i for i in range(n+1)]
rank = [1] * (n+1)
def find(x):
    while x != par[x]:
        par[x] = par[par[x]]
        x = par[x]
    return x
def union(x1, x2):
    p1, p2 = find(x1), find(x2)
    if p1 == p2:
        return False
    if rank[p1] > rank[p2]:
        par[p2] = p1
        rank[p1] += rank[p2]
    else:
        par[p1] = p2
        rank[p2] += rank[p1]
    return True
for _ in range(n-1):
    x,y = map(int,input().split())
    nodes.add(x)
    nodes.add(y)
    union(x,y)
    union(y,x)
print(par)