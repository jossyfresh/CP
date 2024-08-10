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
    a,b,c,n = li()
    arr = [a,b,c]
    arr.sort()
    x = arr[-1] - arr[0]
    y = arr[-1] - arr[1]

    if x + y <= n and (n - x - y) % 3 == 0:
        print("YES")
    else:
        print("NO")

    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
