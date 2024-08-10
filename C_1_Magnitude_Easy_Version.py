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
    arr.insert(0,0)
    dp = [0] * (n + 1)
    dpp = [0] * (n + 1)
    for i in range(1, n + 1):
        dpp[i] = dpp[i - 1] + arr[i]
        dp[i] = max(dp[i - 1] + arr[i], abs(dpp[i - 1] + arr[i]))
    print(dp[n])
if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()