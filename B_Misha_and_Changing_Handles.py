from collections import defaultdict
n = int(input())
adjlist = defaultdict(list)
let = []
for _ in range(n):
    x,y = map(str,input().split())
    adjlist[x].append(y)
    let.append((x,y))
def dfs(cur):
    visited.add(cur)
    if cur not in adjlist:
        return cur
    for node in adjlist[cur]:
        if node not in visited:
            visited.add(node)
            return dfs(node)
        else:
            return cur
visited = set()
ans = []
for x,y in let:
    if x not in visited:
        ans.append(f'{x} {dfs(x)}')
print(len(ans))
for x in ans:
    print(x)




