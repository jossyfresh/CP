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



def prime_factors(n):
    i = 2
    while n % i == 0:
        n = n // i
    if n == 1:
        return True
    return False


def solve():
    # Start here
    n = intp()
    print('NO' if prime_factors(n) else 'YES')
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
