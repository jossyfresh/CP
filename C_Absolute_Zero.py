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
    arr.sort()
    for i in range(1,n):
        if arr[i] % 2 != arr[0] % 2:
            print(-1)
            return
    print(40)
    ans = []
    for i in range(0,40):
        mn = min(arr)
        mx = max(arr)
        mid = (mn+mx)//2
        ans.append(mid)
        for i in range(len(arr)):
            arr[i] = abs(arr[i] - mid)
    print(*ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
