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
    n,k = map(int, input().split())
    arr = li()
    a = li()
    l = 0
    r = 5*(10**8)
    def check(x):
        res = 0
        for i in range(len(a)):
            if x > arr[i]:
                res += a[i]
            else:
                res += math.ceil(arr[i] / x) * a[i]
        if res > k:
            return False
        else:
            return True
    while r - l > 1:
        m = (r + l) // 2
        if check(m):
            r = m
        else:
            l = m
    if r == 5*(10**8):
        print(-1)
    else:
        print(r)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
