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
    s = string()
    s = s.lower()
    vowels = "aeiouy"
    ans = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            ans += "." + s[i]
    print(ans)

    return

if __name__ == "__main__":
    fast_io()
    solve()
