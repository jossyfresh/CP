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
    mod = 10**9+7
    n,k = map(int,input().split())
    nums = li()
    max_sum = sum(nums)
    dp = [0]*len(nums)
    dp[0] = nums[0]
    ans = dp[0]
    for i in range(1,len(nums)):
        dp[i] = max(nums[i],nums[i]+dp[i-1])
        ans = max(ans,dp[i])
    if ans < 0:
        print(max_sum % mod)
    else:
        rest = max_sum - ans
        ans = (2**k) * ans
        print((ans+rest) % mod)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
