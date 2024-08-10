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


def reverse_bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo
def reverse_bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: lo = mid+1
        else: hi = mid
    return lo

def solve():
    # Start here
    n,f,k = li()
    arr = li()
    val = arr[f-1]

    arr.sort(reverse=True)

    l = 0
    r = 0
    flag = True
    for i in range(len(arr)):
        if arr[i] == val:
            if l == 0 and flag:
                l = i
                flag = False
            r = i

    
    if l <= k-1 and r > k-1:
        print("MAYBE")
    elif l <= k-1 and r <= k-1:
        print("YES")
    else:
        print("NO")

    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
