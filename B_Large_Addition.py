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
    n = input()
    if int(n[0]) != 1:
        print("NO")
        return
    if int(n[-1]) == 9:
        print("NO")
        return
    for i in range(len(n)-1):
        if int(n[i]) == 0:
            print("NO")
            return
    print("YES")
    return


if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
