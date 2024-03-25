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

def cycle_detection_directed(graph):
    def dfs(node):
        visited.add(node)
        on_stack.add(node)
        for neighbor in graph[node]:
            if neighbor in on_stack:
                return True
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        on_stack.remove(node)
        return False

    visited = set()
    on_stack = set()
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

def solve():
    # Start here
    n,a,b = map(int, input().split())
    adj = defaultdict(list)
    for i in range(2):
        x,y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    print(adj)
    if cycle_detection_directed(adj):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
