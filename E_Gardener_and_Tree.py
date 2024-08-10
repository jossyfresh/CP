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
    empty = input()
    n,k = li()
    adj = defaultdict(list)
    indegree = defaultdict(int)

    for i in range(n-1):
        u,v = li()
        adj[u].append(v)
        adj[v].append(u)
        indegree[u] += 1
        indegree[v] += 1
    
    queue = deque()

    for i in range(1,n+1):
        if indegree[i] == 1 or indegree[i] == 0:
            queue.append(i)
    while queue and k > 0:
        l = len(queue)
        while l:
            l -= 1
            cur = queue.popleft()
            n -= 1
            for node in adj[cur]:
                indegree[node] -= 1
                if indegree[node] == 1:
                    queue.append(node)
        k -= 1
    
    print(n)

    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
