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
    n,m = li()
    a = input()
    count = Counter(a)
    ans = 0
    v = ["A","B","C","D","E","F","G"]
    for x in v:
        if x not in count:
            ans += m
        else:
            
            if m > count[x]:
                ans += m - count[x]
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
