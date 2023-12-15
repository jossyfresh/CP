n,d  = map(int,input().split())
rep = {i:i for i in range(1,n+1)}
size = {i:1 for i in range(1,n+1)}
def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]
def union(x,y):
    repx = find(x)
    repy = find(y)
    if repx == repy:
        return 
    if size[repx] > size[repy]:
        rep[repy] = repx
        size[repx] += size[repy] 
        size[repy] = 1
    else:
        rep[repx] = repy
        size[repy] += size[repx]
        size[repx] = 1
k = 1
for _ in range(d):
    ans = []
    res = 0
    x,y = map(int,input().split())
    if find(x) == find(y):
        k += 1
    else:
        union(x,y)
    for x in size:
        ans.append(size[x])
    ans.sort(reverse=True)
    for i in range(k):
        res += ans[i]
    print(res -1)




