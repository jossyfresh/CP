n,m = map(int,input().split())
rep = {i:i for i in range(1,n+1)}
size = {i:1 for i in range(1,n+1)}
visited = set()
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
    else:
        rep[repx] = repy
        size[repy] += size[repx]
for _ in range(m):
    num = list(map(int,input().split()))
    for i in range(1,len(num)-1):
        if (num[i],num[i+1]) not in visited:
            union(num[i],num[i+1])
            visited.add((num[i],num[i+1]))
ans = []
for i in range(1,n+1):
    val = find(i)
    ans.append(size[val])
print(*ans)

