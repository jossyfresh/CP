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
    arr2 = li()
    ans = 0
    val = arr2[-1]
    add = 1
    chage = float('inf')
    for i in range(n):
        mx = max(arr[i], arr2[i])
        mn = min(arr[i], arr2[i])
        if mn <= val <= mx:
            add = 0
        ans += abs(arr[i] - arr2[i])
        chage = min(chage, abs(val - mn), abs(val - mx))
    ans += chage * add + 1
    print(ans)
        
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
