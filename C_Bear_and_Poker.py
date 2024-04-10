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
    a = li()
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
        while a[i] % 3 == 0:
            a[i] //= 3
    for i in range(n):
        if a[i] != a[0]:
            print('No')
            return
    print('Yes')
    return

if __name__ == "__main__":
    fast_io()
    solve()
