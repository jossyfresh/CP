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

primes = set()
def bitwiseSieve(srt, n):
    prime = [0 if i % 2 == 0 else 1 for i in range(n+1)]
    prime[1] = 0
    prime[2] = 1
    i = 3
    while (i * i <= n):
        if (prime[(i)] == 1):
            j = i * i
            while (j <= n):
                prime[j] = 0
                j += 2*i
        i += 2
    i = srt
    while (i <= n):
        if (prime[i] == 1):
            primes.add(i)
        i += 1

def solve():
    # Start here
    n = intp()
    # edges = set()
    # bitwiseSieve(2,10**5)
    # for i in range(1,n+1):
    #     for j in range(1,n+1):
    #         if i == j:
    #             continue
    #         if i ^ j in primes:
    #             if (j,i,i^j) not in edges:
    #                 edges.add((i,j,i ^ j))
    # print(edges)
    # print("edges",len(edges)//2)
    def check(n):
        if n == 1:
            return 1
        if n == 2 or n == 3:
            return 2
        if n == 4 or n == 5:
            return 3
        if n >= 6:
            return 4
    colors = []
    def color(n,num):
        if n == 1:
            colors.append(1)
            return
        if n == 2:
            colors.append(1)
            colors.append(2)
            return
        if n == 3:
            colors.append(1)
            colors.append(2)
            colors.append(2)
            return
        if n == 4:
            colors.append(1)
            colors.append(2)
            colors.append(2)
            colors.append(3)
            return
        if n == 5:
            colors.append(1)
            colors.append(2)
            colors.append(2)
            colors.append(3)
            colors.append(3)
            return
        if n == 6:
            colors.append(1)
            colors.append(2)
            colors.append(2)
            colors.append(3)
            colors.append(3)
            colors.append(4)
            return
        curr = 1
        for i in range(1,n+1):
            colors.append(curr)
            curr = (curr % num) + 1
    number = check(n)
    color(n,number)
    print(number)
    print(*colors)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
