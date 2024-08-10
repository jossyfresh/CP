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
    s = "BAN" * n
    if n == 1:
        print(1)
        print(1,2)
        return
    b = [i+1 for i in range(len(s)) if s[i] == "B"]
    N = [i+1 for i in range(len(s)) if s[i] == "N"]
    ans = []
    i = 0
    j = len(N) -1
    while b[i] < N[j]:
        ans.append([b[i],N[j]])
        i += 1
        j -= 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i]) 

    
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
