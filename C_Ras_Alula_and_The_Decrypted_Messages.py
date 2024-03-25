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
    n,m = map(int, input().split())
    s = input()
    w = input()
    win = 0
    st = 0
    for i in range(len(w)):
        win += ord(w[i])
    for i in range(len(w)):
        st += ord(s[i])
    l = 0
    r = len(w)
    while r < n:
        if st == win:
            print("YES")
            return
        st -= ord(s[l])
        st += ord(s[r])
        l += 1
        r += 1
    if st == win:
        print("YES")
    else:
        print("NO")
    return
 
if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()