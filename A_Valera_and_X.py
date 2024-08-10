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
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == j or i+j == n-1:
                if grid[i][j] != grid[0][0] or grid[i][j] == grid[0][1]:
                    print("NO")
                    return
            else:
                if grid[i][j] != grid[0][1] or grid[i][j] == grid[0][0]:
                    print("NO")
                    return
    print("YES")
    return

if __name__ == "__main__":
    fast_io()
    solve()
