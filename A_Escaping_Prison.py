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
    n,h = map(int, input().split())
    ans = 0
    for i in range(n):
        x,y = map(int, input().split())
        ans += max(x,y)
    if ans < h:
        print("NO")
    else:
        print("YES")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
