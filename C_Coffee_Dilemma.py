import sys,math,os,heapq
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
    heap = []
    heapq.heapify(heap)
    sum = 0
    ans = 0
    for i in range(len(arr)):
        sum += arr[i]
        heapq.heappush(heap,(arr[i],i))
        if sum < 0:
            while sum < 0:
                sum -= heapq.heappop(heap)[0]
        ans = max(ans,len(heap))
    res = []
    for x in heap:
        res.append(x)
    res.sort(key=lambda x:x[1])
    res = [x[0] for x in res]
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    solve()
