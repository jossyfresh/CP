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
    n = intp()
    arr = li()
    adj = defaultdict(list)
    edges = li()
    for i in range(len(edges)):
        u = i+2
        v = edges[i]
        adj[v].append(u)
    
    print(adj)

    def dfs(node):
        if not adj[node]:
            return arr[node-1]
        res = float("inf")
        for child in adj[node]:
            res = min(res,dfs(child))
        if arr[node-1] > res:
            return res
    print(dfs(1) + arr[0])
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
