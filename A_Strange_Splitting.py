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
    n = int(input())
    arr = li()
    if len(set(arr)) == 1:
        print("NO")
        return
    print("YES")
    ans = ""
    if len(set(arr[1:])) == 1:
        ans += "RR"
        for i in range(2,n):
            ans += "B"
        print(ans)
        return
    ans += "R"
    for i in range(1,n):
        ans += "B"
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
