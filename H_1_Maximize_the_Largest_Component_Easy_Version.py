import sys,math,os
from collections import defaultdict, deque, Counter, OrderedDict, namedtuple
from bisect import bisect_right, bisect_left

def li(): return list(map(int, sys.stdin.readline().strip().split()))
def intp(): return int(sys.stdin.readline().strip())

def string():
    return sys.stdin.readline().strip()

def fast_io():
    sys.stdin = open(0)
    sys.stdout = open(1, "w")

# union find by size with path compresion



def solve():
    # Start here
    n,m = li()
    grid = []
    parent = {}
    size = {}
    for i in range(n):
        for j in range(m):
            parent[(i,j)] = (i,j)
            size[(i,j)] = 1
    def union(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] > size[y]:
            x,y = y,x
        parent[x] = y
        size[y] += size[x]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    for i in range(n):
        line = input()
        grid.append(line)
    for i in range(len(grid)):
        for j in range(len(grid[i])-1):
            if grid[i][j] == grid[i][j+1] == '#':
                union((i,j),(i,j+1))
    for j in range(m):
        for i in range(n-1):
            if grid[i][j] == grid[i+1][j] == '#':
                union((i,j),(i+1,j))

    count = Counter()
    for key in parent:
        count[find(key)] += 1
    ans = 0
    for i in range(n):
        res = size[find((i,0))]
        key = (i,0)
        for j in range(1,m):
            if i > 0:
                key2 = (i-1,j)
                if find(key2) != find(key) and grid[i-1][j] == '#':
                    res += 1
            if i < n-1:
                key3 = (i+1,j)
                if find(key3) != find(key)  and grid[i+1][j] == '#': 
                    res += 1
        ans = max(res,ans)
    for j in range(m):
        res = size[find((0,j))]
        key = (0,j)
        for i in range(n):
            key1 = (i,j)
            if find(key1) != find(key):
                res += size[find(key1)]
            if j > 0:
                key2 = (i,j-1)
                if find(key2) != find(key) and grid[i][j-1] == '#':
                    res += size[find(key2)]
            if j < m-1:
                key3 = (i,j+1)
                if find(key3) != find(key) and grid[i][j+1] == '#':
                    res += size[find(key3)]
        ans = max(res,ans)
    print(ans)

    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
