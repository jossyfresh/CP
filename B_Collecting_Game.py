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
    for i in range(len(arr)):
        arr[i] = [arr[i],i]
    arr.sort()
    ans = [0]*n
    prev = arr[0][0]
    c = 0
    s = 0
    start = 0
    for i in range(1,len(arr)):
        if prev < arr[i][0]:
            for j in range(start,i):
                ans[arr[j][1]] = c
            start = i
        c += 1
        prev += arr[i][0]
    for i in range(start,n):
        ans[arr[i][1]] = c
    print(*ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
