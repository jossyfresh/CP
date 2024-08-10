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
    n,s,m = li()
    interval = []
    for i in range(n):
        x,y = li()
        interval.append((x,y))
    interval.sort()
    if interval[0][0] >= s:
        print("YES")
        return
    for i in range(1,n):
        if interval[i][0] - interval[i-1][1] >= s:
            print("YES")
            return
    if interval[-1][1] + s <= m:
        print("YES")
        return
    print("NO")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
