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
    arr = li()
    ans = 0
    for i in range(len(arr)):
        x = [i+1,arr[i]]
        x.sort()
        arr[i] = tuple(x)
    vi = set()
    for x in arr:
        if x in vi:
            ans += 1
        vi.add(x)
    if ans > 0:
        print(2)
    else:
        print(3)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
