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
    n,m = li()
    grida = []
    for i in range(n):
        grida.append(list(string()))
    gridb = []
    for i in range(n):
        gridb.append(list(string()))
    ans1 = []
    for i in range(n):
        suma = 0
        for j in range(m):
            suma += int(grida[i][j])
        ans1.append(suma % 3)
    ans2 = []
    for i in range(n):
        sumb = 0
        for j in range(m):
            sumb += int(gridb[i][j])
        ans2.append(sumb % 3)

    if ans1 == ans2:
        print("YES")
    else:
        print("NO")

    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
