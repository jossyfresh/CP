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


def check(arr):
    l = 0
    m = 1
    r = 2
    while r < len(arr):
        x = math.gcd(arr[l],arr[m])
        y = math.gcd(arr[m],arr[r])
        if x > y:
            return False
        l += 1
        m += 1
        r += 1
    return True

def solve():
    # Start here
    n = int(input())
    arr = li()
    ans = []
    if len(arr) == 3:
        print("YES")
        return
    l = 0
    m = 1
    r = 2
    flag = True
    while r < len(arr):
        x = math.gcd(arr[l],arr[m])
        y = math.gcd(arr[m],arr[r])
        if x > y:
            res = False
            new = []
            for i in range(len(arr)):
                if i == m-1:
                    continue
                else:
                    new.append(arr[i])
            res = res or check(new)
            new = []
            for i in range(len(arr)):
                if i == m:
                    continue
                else:
                    new.append(arr[i])
            res = res or check(new)
            new = []
            for i in range(len(arr)):
                if i == m+1:
                    continue
                else:
                    new.append(arr[i])
            res = res or check(new)
            if res:
                print("YES")
                return
            else:
                print("NO")
                return
        l += 1
        m += 1
        r += 1
    print("YES")
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
