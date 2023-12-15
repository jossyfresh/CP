n,m = map(int,input().split())
people = {}
p = {}
for i in range(n):
    x = input()
    people[i] = x
    p[x] = i
graph = [[True for i in range(n)] for i in range(n)]
for _ in range(m):
    x,y = map(str,input().split())
    x = p[x]
    y = p[y]
    graph[x][y] = False
    graph[y][x] = False
maxsize = 0
ans = []
for x in range(2**n):
    valid = True
    team = []
    for i in range(n):
        if (x & (1 << i)):
            for node in team:
                if graph[i][node] == False:
                    valid = False
                    break
            team.append(i)
        if not valid:
            break
    if len(team) > maxsize and valid:
        ans = team
        maxsize = len(team)
res = []
for x in ans:
    res.append(people[x])
res.sort()
print(len(res))
for x in res:
    print(x)
