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
    a = int(input())
    b = int(input())
    c = int(input())
    ans = 0
    while c > 3 and b > 1 and a > 0:
        c -= 4
        b -= 2
        a -= 1
        ans += (4 + 2 + 1)
    print(ans)


    return

if __name__ == "__main__":
    fast_io()
    solve()
