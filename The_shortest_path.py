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
    a,b = li()
    adj = defaultdict(list)
    for i in range(m):
        x,y = li()
        adj[x].append(y)
        adj[y].append(x)


    visited = set()
    q = deque()

    q.append((a,str(a)))
    visited.add(a)
    len_ = float('inf')
    ans = ""
    while q:
        n = len(q)
        while n:
            n -= 1
            node,path = q.popleft()
            if node == b:
                if len(path) < len_:
                    len_ = len(path)
                    ans = path
            for nei in adj[node]:
                prev[nei] = node
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei,path + " " + str(nei)))
    if ans != "":
        print(len(ans)-1)
        print(" ".join(ans))
    else:
        print(-1)
    return

if __name__ == "__main__":
    fast_io()
    solve()
