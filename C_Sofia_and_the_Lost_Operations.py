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
    m = intp()
    d = li()
    c = Counter(d)
    diff = defaultdict(int)
    vi = set()
    for i in range(len(a)):
        if a[i] != b[i]:
            diff[b[i]] += 1
        vi.add(b[i])
    flag = False
    if not diff:
        if d[-1] in b:
            print("YES")
            return
    for x in d: 
        if x in diff:
            flag = True
            diff[x] -= 1
        elif x in vi:
            flag = True
        else:
            flag = False
    res = True
    for x in diff:
        if diff[x] > 0:
            res = False
            break
    if flag and res:
        print("YES")
    else:
        print("NO")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
