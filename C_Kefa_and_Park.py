from collections import defaultdict
n,m = map(int,input().split())
cat = list(map(int,input().split()))
adjlist = defaultdict(list)
for _ in range(n-1):
    x,y = map(int,input().split())
    adjlist[x-1].append(y-1)
    adjlist[y-1].append(x-1)
visited = set()
stack = [(-1, 0, cat[0])]
ans = 0
while stack:
    par,cur,cats = stack.pop()
    if cats > m:
        continue
    visited.add(cur)
    for node in adjlist[cur]:
        if node not in visited:
            if cat[node] == 1:
                stack.append((cur,node,cats + cat[node]))
            else:
                stack.append((cur,node,0))
    if len(adjlist[cur]) == 1 and cur != 0:
        ans += 1
print(ans)
	
	
