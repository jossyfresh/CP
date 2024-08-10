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

def solve():
    # Start here
    n,m = li()
    grid = []
    for i in range(n):
        line = input()
        grid.append(line)
    ci,cj = 0,0
    rowl = 0
    coll = 0
    for i in range(len(grid)):
        c = 0
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                c += 1
        if c > rowl:
            rowl = c
            ci = i
    for j in range(m):
        c = 0
        for i in range(n):
            if grid[i][j] == '#':
                c += 1
        if c > coll:
            coll = c
            cj = j


    print(ci+1,cj+1)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
