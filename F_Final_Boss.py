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
    h,n = li()
    arr = li()
    crr = li()
    if sum(arr) >= h:
        print(1)
        return 
    new = list(zip(arr,crr))
    new.sort(key = lambda x: x[1])
    def check(tu):
        total = 0
        for i in range(len(new)):
            total += math.ceil(tu / new[i][1]) * new[i][0]
        return total >= h
    l = 1
    r = 10**18
    while l < r:
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(l)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
