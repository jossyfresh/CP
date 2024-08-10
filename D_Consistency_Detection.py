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
    for i in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        a=[l[0]/(n-k+1)]
        ans='Yes'
        for j in range(1,k):
            a.append(l[j]-l[j-1])
            if a[-1]<a[-2]:
                ans='No'
                break
        print(ans)
    return

if __name__ == "__main__":
    fast_io()
    solve()
