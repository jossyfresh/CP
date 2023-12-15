from collections import defaultdict
n,m  = map(int,input().split())
adjlist = defaultdict(list)
colors = [-1 for i in range(n)]
edges = []
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    adjlist[x].append(y)
    adjlist[y].append(x)
    edges.append((x,y))

flag = 0
stack = [(0)]
colors[0] = 0
while stack:
    cur_node = stack.pop()
    color = colors[cur_node]
    for node in adjlist[cur_node]:
        if colors[node] == -1:
            colors[node] = 1 - color
            stack.append((node))
        else:
            if colors[node] == color:
                flag = 1
                break
    if flag:
        break
ans = []
if flag:
    print("NO")
else:
    print("YES")
    for i in range(m):
        if colors[edges[i][0]] < colors[edges[i][1]]:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))



