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
    arrs = li()
    def mergeSort(arr,l,r):
        if l < r:
            m = l + (r - l) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]
        i = 0
        j = 0
        newl = []
        newr = []
        ll = sorted(L)
        rr = sorted(R)
        for i in range(len(L)):
            val = L[i]
            indx = bisect_left(rr,val)
            newl.append(L[i] + indx)
        for i in range(len(R)):
            val = R[i]
            indx = bisect_left(ll,val)
            newr.append(R[i] + indx)
        for i in range(len(newl)):
            arr[l] = newl[i]
            l += 1
        for i in range(len(newr)):
            arr[l] = newr[i]
            l += 1
    arr = mergeSort(arrs,0,len(arrs)-1)
    print(*arrs)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
