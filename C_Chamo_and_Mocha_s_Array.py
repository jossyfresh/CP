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
    n = int(input())
    arr = li()
    if n == 2:
        print(min(arr))
        return
    ans = deque([arr[0], arr[1], arr[2]])
    val = sorted(ans)[1]
    for j in range(3, n):
        val = max(val,sorted(ans)[1])
        ans.popleft()
        ans.append(arr[j])
        j += 1
    val = max(val,sorted(ans)[1])
    print(val)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
