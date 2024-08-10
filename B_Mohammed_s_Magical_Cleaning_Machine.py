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
    start = 0
    flag = 0
    for i in range(n):
        if arr[i] != 0:
            start = i
            flag = 1
            break
    ans = 0
    if flag == 0:
        print(0)
        return 
    for i in range(start,n-1):
        if arr[i] == 0:
            ans += 1
        else:
            ans += arr[i]
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
