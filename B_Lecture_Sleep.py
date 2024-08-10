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
    n,k = li()
    arr = li()
    arr2 = li()
    start = 0 
    for i in range(n):
        if arr2[i] == 1:
            start += arr[i]
    l = 0
    r = k
    add = 0
    for i in range(k):
        if arr2[i] == 0:
            add += arr[i]
    ans = start + add
    l = 0
    for i in range(k,n):
        if arr2[l] == 0:
            add -= arr[l]
        if arr2[i] == 0:
            add += arr[i]
        l += 1
        ans = max(ans, start + add)
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    solve()
