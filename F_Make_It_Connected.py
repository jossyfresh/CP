from collections import defaultdict
n,m = map(int,input().split())
rep = {i:i for i in range(n)}
rank = [0] * n
def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]
def union(x,y):
    repx = find(x)
    repy = find(y)
    if repx == repy:
        return 
    if rank[repx] < rank[repy]:
        repx,repy = repy,repx
    rep[repy] = repx
    if rank[repx] == rank[repy]:
        rank[repx] += 1
num = list(map(int,input().split()))
val = 10**12
ind = 0
for i in range(len(num)):
    if val > num[i]:
        val = num[i]
        ind = i
    num[i] = (num[i],i)
edges = []
for i in range(m):
    x,y,z = map(int,input().split())
    edges.append((x-1,y-1,z))
for i in range(len(num)):
    if i != ind:
        edges.append((ind,num[i][1],val + num[i][0]))
edges.sort(key=lambda x:x[2])
ans = 0
k = 0
for x,y,z in edges:
    if find(x) != find(y):
        ans += z
        union(x,y)
        k += 1
        if k == n-1:
            break
print(ans)
