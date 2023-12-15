n,m = map(int,input().split())
grid = []
rep = {}
size = {}
for i in range(n):
    for j in range(m):
        rep[(i,j)] = (i,j)
        size[(i,j)] = 1
def inbound(i,j):
    return 0<=i<n and 0<=j<m
direction = [(-1,0),(1,0),(0,1),(0,-1)]
def find(x):    
    if (rep[x] != x):
        rep[x] = find(rep[x])
    return rep[x]
def union(x,y):
    repx = find(x)
    repy = find(y)
    if repx != repy:
        if size[repx] > size[repy]:
            rep[repy] = repx
            size[repx] += size[repy]
        else:
            rep[repx] = repy
            size[repy] += size[repx]
visited = set()
def dfs(i,j):
    for x,y in direction:
        ni = x + i
        nj = y + j
        if inbound(ni,nj) and (ni,nj) not in visited and grid[ni][nj] == ".":
            visited.add((ni,nj))
            union((ni,nj),(i,j))
            dfs(ni,nj)
for i in range(n):
    s = input()
    grid.append(list(s))
print(grid)
visited = set()
for i in range(len(grid)):
    for j in range(m):
        if grid[i][j] == ".":
            dfs(i,j)
for i in range(len(grid)):
    for j in range(m):
        if grid[i][j] == "*":
            ans = 0
            visited = set()
            for x,y in direction:
                ni = x + i
                nj = y + j
                if inbound(ni,nj) and grid[ni][nj] == ".":
                    parent = find((ni,nj))
                    if parent not in visited:
                        ans += size[parent]
                        visited.add(parent)
            grid[i][j] = (ans+1)%10
for x in grid:
    s = ""
    for y in x:
        s += f'{y}'
    print(s)