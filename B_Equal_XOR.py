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
    n,k = map(int,input().split())
    m1 = set()
    m2 = set()
    arr = li()
    for i in range(len(arr)):
        if i > n-1:
            m2.add(arr[i])
        else:
            m1.add(arr[i])
    ans1 = []
    ans2 = []
    for i in range(1,n+1):
        if i in m1 and i not in m2:
            ans1.append(i)
            ans1.append(i)
        if len(ans1) == (2 * k):
            break
    for i in range(1,n+1):
        if i in m2 and i not in m1:
            ans2.append(i)
            ans2.append(i)
        if len(ans2) == (k*2):
            break
    for i in range(1,n+1):
        if i in m1 and i in m2:
            if len(ans1) < (2 * k):
                ans1.append(i)
            if len(ans2) < (2 * k):
                ans2.append(i)
    print(*ans1)
    print(*ans2)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
