t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    grid = []
    mat = []
    let = "vika"
    for _ in range(n):
        s = input()
        grid.append(s)
    l = 0
    for i in range(m):
        x = []
        for j in range(n):
            x.append(grid[j][i])
        if let[l] in x:
            l += 1
    if l == len(let):
        print("YES")
    else:
        print("NO")