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
    parent = [i for i in range(n)]
    size = [1]*n
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x,y = y,x
        parent[y] = x
        size[x] += size[y]
    arr = li()

    for i in range(len(arr)):
        union(i,arr[i]-1)
    print(len(set([find(i) for i in range(n)])))

    return

if __name__ == "__main__":
    fast_io()

    solve()
