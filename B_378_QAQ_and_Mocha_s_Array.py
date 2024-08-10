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
    a = arr[0]
    b = 0
    for i in range(1, n):
        if arr[i] % a != 0:
            b = arr[i]
            break
    for i in range(2, n):
        if (arr[i] % a == 0 ) or (arr[i] % b == 0):
            continue
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
