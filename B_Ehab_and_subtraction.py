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
    arr = list(set(arr))
    arr.sort()
    minus = 0
    for i in range(k):
        if i >= len(arr):
            print(0)
        else:
            arr[i] -= minus
            print(arr[i])
            minus += arr[i]
    return

if __name__ == "__main__":
    fast_io()
    solve()
