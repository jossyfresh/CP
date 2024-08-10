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

def reverse(s,p):
    start = s[:p+1]
    end = s[p+1:]
    return start[::-1] + end

def shift(s,p):
    start = s[:p+1]
    end = s[p+1:]
    return end + start

def check(s,k):
    section = ""
    prev = ""
    for i in range(len(s)):
        section += s[i]
        if len(section) == k:
            for j in range(len(section)-1):
                if section[j] != section[j+1]:
                    return False
            if prev == section:
                return False
            prev = section[-1]
            section = ""
    return True

def solve():
    # Start here
    n,k = li()
    str = string()
    for i in range(n):
        val = reverse(str,i)
        shifted = shift(val,i)
        if check(shifted,k):
            print(i+1)
            return
    print(-1)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
