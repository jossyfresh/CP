n = int(input())
qi,qj = map(int,input().split())
ki,kj = map(int,input().split())
ci,cj = map(int,input().split())
c = n - qj
d = qi - 1
qi = c
qj = d
h = n - cj
l = ci - 1
ci = h
cj = l
a = n - kj
b = ki - 1
ki = a
kj = b
matrix = [[0 for i in range(n)] for x in range(n)]
def down(qi,qj):
    while qi < n:
        matrix[qi][qj] = 1
        qi += 1
def right(qi,qj):
    while qj < n:
        matrix[qi][qj] = 1
        qj += 1
def up(qi,qj):
    while qi >= 0:
        matrix[qi][qj] = 1
        qi -= 1
def left(qi,qj):
    while qj >= 0:
        matrix[qi][qj] = 1
        qj -= 1
def leftu(qi,qj):
    while qi >= 0 and qj >= 0:
        matrix[qi][qj] = 1
        qi -= 1
        qj -= 1
def rightu(qi,qj):
    while qi >= 0 and qj < n:
        matrix[qi][qj] = 1
        qi -= 1
        qj += 1
def rightd(qi,qj):
    while qi < n and qj < n:
        matrix[qi][qj] = 1
        qi += 1
        qj += 1
def leftd(qi,qj):
    while qi < n and qj >= 0:
        matrix[qi][qj] = 1
        qi += 1
        qj -= 1
left(qi,qj)
right(qi,qj)
up(qi,qj)
down(qi,qj)
leftu(qi,qj)
rightu(qi,qj)
rightd(qi,qj)
leftd(qi,qj)
visited = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(-1,-1),(1,-1),(-1,1),(1,1)]
ans = [False]
def inbound(row, col):
    return (0 <= row < n and 0 <= col < n)
def dfs(ki,kj):
    if ki == ci and kj == cj:
        ans[0] = True
        return 
    for row_change, col_change in directions:
        kii = ki + row_change
        kjj = kj + col_change

        if inbound(kii, kjj) and (kii,kjj) not in visited and matrix[kii][kjj] == 0:
            visited.add((kii,kjj))
            dfs(kii,kjj)


dfs(ki,kj)
print()
if ans[0]:
    print("YES")
else:
    print("NO")