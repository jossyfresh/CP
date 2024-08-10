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
    if k > 2:
        print(0)
    elif k == 1:
        min_ = min(arr)
        arr.sort()
        for i in range(n-1):
            min_ = min(min_,abs(arr[i] - arr[i+1]))
        print(min_)
    else:
        res = min(arr)
        arr.sort()
        for i in range(n):
            for j in range(i+1,n):
                val = abs(arr[i] - arr[j])
                res = min(res,val)
                r = bisect_right(arr,val)
                if r-1 >= 0:
                    res = min(abs(arr[r-1] - val),res)
                if r + 1 < n:
                    res = min(abs(arr[r+1] - val),res)
                res = min(abs(arr[r] - val),res)
        print(res)            
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
