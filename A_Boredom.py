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
    arr = li()
    counter = Counter(arr)
    dp = [0] * (max(arr) + 1)
    dp[0] = 0
    dp[1] = counter[1]
    for i in range(2, max(arr)+1):
        dp[i] = max(dp[i-1], dp[i-2] + i * counter[i])
    print(dp[-1])

    return

if __name__ == "__main__":
    fast_io() 
    solve()
