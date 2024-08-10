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
    i = intp()
    count = 0
    for n in range(1,i+1):
        factorization = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factorization.append(d)
                n //= d
            d += 1
        if n > 1:
            factorization.append(n)
        print(factorization)
        if len(set(factorization)) == 2:
            count += 1
    print(count)

    return

if __name__ == "__main__":
    fast_io()
    solve()
