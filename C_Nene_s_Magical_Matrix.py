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
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    a = 0
    b = 0
    for i in range(1, 2 * n + 1):
        if i & 1:
            val = n
            for j in range(n):
                arr[a][j] = val
                val -= 1
            a += 1
        else:
            val = n
            for i in range(n):
                arr[i][b] = val
                val -= 1
            b += 1
    total = sum(sum(row) for row in arr)
    l = 1
    r = 1
    ans = [i for i in range(n, 0, -1)]
    print(total, 2 * n)
    for i in range(1, 2 * n + 1):
        if i & 1:
            print(1, l, *ans)
            l += 1
        else:
            print(2, r, *ans)
            r += 1
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
