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
    a,b = li()
    kingx,kingy = li()
    queenx,queeny = li()
    knightk = set()
    knightq = set()
    moves = [(a,b),(b,a),(a,-b),(-b,a),(-a,b),(b,-a),(-a,-b),(-b,-a)]
    for i in moves:
        nx = kingx + i[0]
        ny = kingy + i[1]
        knightk.add((nx,ny))
    for i in moves:
        nx = queenx + i[0]
        ny = queeny + i[1]
        knightq.add((nx,ny))
    ans = 0
    for i in knightk:
        if i in knightq:
            ans += 1
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
