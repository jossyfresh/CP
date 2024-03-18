import sys
import math,random
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
    a.sort()
    val = random.randint(0,10**4)
    mp = defaultdict(int)
    for i in range(len(a)):
        v = a[i] ^ val
        mp[v] += 1
    flag = False
    for i in range(0,n+1):
        z = i ^ val
        if mp[z] == 0:
            print(i)
            return
        if flag and mp[z] < 2:
            print(i)
            return
        if mp[z] == 1:
            flag = True
    return
if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
