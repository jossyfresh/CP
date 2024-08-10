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
    n,q = li()
    c = li()
    adj = defaultdict(list)
    for i in range(n-1):
        u, v = li()
        adj[u].append(v)
        adj[v].append(u)
    for i in range(q):
        u = intp()
        c[u-1] = 1 - c[u-1]
    q = deque()
    for i,x in enumerate(c):
        if x == 1:
            q.append(i+1)
    visited = [False] * (n+1)
    while q:
        u = q.popleft()
        visited[u] = True
        for v in adj[u]:
            if c[v-1] == 0:
                print("NO")
                return
            if not visited[v]:
                q.append(v)
    print("YES")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
