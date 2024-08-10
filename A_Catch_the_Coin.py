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
    n,q = li()
    a = input()
    b = input()
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        l = 0
        for j in range(n):
            if a[i] != b[j]:
                l += 1
            dp[i][j] = l
    print(dp)
    for _ in range(q):
        l,r = li()
        l -= 1
        r -= 1
        print(dp[l][r])
    
    return

if __name__ == "__main__":
    fast_io()
    t = intp()
    for _ in range(t):
        solve()
