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
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = []
    for i in range(len(a)):
        if a[i] < b[i]:
            arr.append((a[i],b[i]))
    arr.sort(key=lambda x: x[0])
    alice = 0
    for i in range(len(arr)):
        alice += arr[i][0]
        k -= 1
        if k <= 0:
            bob += arr[i][1]
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
