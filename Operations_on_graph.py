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
    k = intp()
    adj = defaultdict(list)
    for i in range(k):
        input = li()
        if input[0] == 1:
            a = input[1]
            b = input[2]
            adj[a].append(b)
            adj[b].append(a)
        else:
            a = input[1]
            if len(adj[a]) > 0:
                print(*adj[a])
    return

if __name__ == "__main__":
    fast_io()
    solve()
