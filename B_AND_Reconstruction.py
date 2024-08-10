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
    b = list(map(int, input().split()))
    start = bin(2**30)[2:]
    ans = [0]*n
    for i in range(n-1):
        ans[i] = ans[i] | b[i]
        ans[i+1] = ans[i+1] | b[i]
    for i in range(n-1):
        if b[i] != (ans[i] & ans[i+1]):
            print(-1)
            return
    print(*ans)
    
    
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
