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
    n = intp()
    a = li()
    b = li()
    for i in range(len(b)):
        b[i] = [b[i],i]
    b.sort(key=lambda x: (x[0],-x[1]))
    for i in range(len(b)):
        
        l = b[i][1]
        r = b[i][1]
        indexl = -1
        indexr = -1
        start = 0
        end = 0
        while l >= 0 and a[l] <= b[i][0]:
            if a[l] == b[i][0]:
                indexl = l
                break
            l -= 1
        while r < n and a[r] <= b[i][0]:
            if a[r] == b[i][0]:
                indexr = r
                break
            r += 1
        if indexr == -1 and indexl == -1:
            print("NO")
            return
        if indexr == -1:
            start = indexl
            end = b[i][1]
        elif indexl == -1:
            start = b[i][1]
            end = indexr
        elif abs(indexr - b[i][1]) > abs(indexl - b[i][1]):
            start = indexl
            end = b[i][1]
        else:
            start = b[i][1]
            end = indexr
        for j in range(start,end+1):
            a[j] = b[i][0]  

    c = [0]*n
    for x in b:
        c[x[1]] = x[0]

    if a == c:
        print("YES")
    else:
        print("NO")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
