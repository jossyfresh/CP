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
    n,k = li()
    arr = li()
    if k == 1:
        print(min(arr))
        return
    if k == 2:
        pre = [arr[0]]*n
        suf = [arr[-1]]*n
        for i in range(1,len(arr)):
            pre[i] = min(pre[i-1],arr[i])
        for i in range(len(arr)-2,-1,-1):
            suf[i] = min(suf[i+1],arr[i])
        ans = float("-inf")
        for i in range(n-1):
            ans = max(ans,max(pre[i],suf[i+1]))
        print(ans)
        return

    print(max(arr))
    
    return

if __name__ == "__main__":
    fast_io()
    solve()


