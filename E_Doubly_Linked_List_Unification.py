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
    n=int(input())
    arr=[[0,0]]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    end = 0
    for i in range(1,n+1):
        if not arr[i][0]:
            arr[end][1]=i
            arr[i][0]=end
            j=i
            while arr[j][1]:
                j=arr[j][1]
            end=j

    for i in range(1,n+1):
        print(*arr[i])
    return

if __name__ == "__main__":
    fast_io()
    solve()

 