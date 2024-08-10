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
    s = input()
    if '0' not in s:
        print(len(s) ** 2)
        return
    if '1' not in s:
        print(0)
        return
    max_ = 0
    count = 0
    for i in range(len(s)*2):
        i = i % len(s)
        if s[i] == '1':
            count += 1
            max_ = max(max_, count)
        else:
            count = 0
    time = 1
    ans = 0
    for i in range(max_,0,-1):
        val = i * time
        time += 1
        ans = max(ans,val)
    print(ans)
        
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
