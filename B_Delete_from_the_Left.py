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
    a = string()
    b = string()
    r1 = len(a)-1
    r2 = len(b)-1
    while r1 >= 0 and r2 >= 0:
        if a[r1] == b[r2]:
            r1 -= 1
            r2 -= 1
        else:   
            break
    print(r1 + 1 + r2 + 1)
    return

if __name__ == "__main__":
    fast_io()
    solve()
