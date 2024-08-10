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

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return abs(a*b) // gcd(a,b)

def solve():
    # Start here
    n = intp()
    arr = li()
    l = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        l = lcm(l,arr[i])
    a = []
    print(l)
    for i in range(len(arr)):
        a.append(l // arr[i])
    total = sum(a)
    flag = True
    for i in range(len(arr)):
        if a[i] * arr[i] <= total:
            flag = False
            break
    if flag:
        print(*a)
    else:
        print(-1)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
