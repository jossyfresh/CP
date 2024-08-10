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

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def solve():
    # Start here
    x, y, z, k = map(int, input().split())
    ans = 0

    divisors = get_divisors(k)
    for d1 in divisors:
        if d1 > x:
            continue
        rem = k // d1
        rem_div = get_divisors(rem)
        for d2 in rem_div:
            if d2 > y:
                continue
            d3 = rem // d2
            if d3 <= z:
                cl = (x - d1 + 1) * (y - d2 + 1) * (z - d3 + 1)
                ans = max(ans, cl)

    print(ans)

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
