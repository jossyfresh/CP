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
    a1,b1,a2,b2 = li()
    ans = 0
    
    if a1 > b1 and a1 > b2 and a2 > b1 and a2 > b2:
        print(4)
        return
    if a1 <= b1 and a1 <= b2 and a2 <= b1 and a2 <= b2:
        print(0)
        return 
    


    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
