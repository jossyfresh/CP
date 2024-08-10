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
    start = 0
    c = 0
    for i in range(len(b)):
        flag = 0
        for j in range(start,len(a)):
            if b[i] == a[j]:
                start = j
                flag = 1
                break
        if not flag:
            c += 1
    print(len(a) + c)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
