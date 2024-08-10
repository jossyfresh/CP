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
    pp = li()
    tt = li()
    arr = list(zip(pp, tt))
    pro = []
    test = []
    for i in range(len(arr)):
        arr[i] = [arr[i][0], arr[i][1], True if arr[i][0] >= arr[i][1] else False]
    nearstT = -1
    nearstP = -1
    
    for i in range(len(arr)-1):
        if len(pro) == n:
            if nearstP == -1 and arr[i][2] == True:
                nearstP = i
            test.append(arr[i][1])
            arr[i][2] = False
        elif len(test) == m:
            if nearstT == -1 and arr[i][2] == False:
                nearstT = i
            pro.append(arr[i][0])
            arr[i][2] = True
        else:
            if arr[i][0] >= arr[i][1]:
                pro.append(arr[i][0])
                arr[i][2] = True
            else:
                test.append(arr[i][1])
                arr[i][2] = False
    val = sum(pro) + sum(test)
    res = []
    for i in range(len(arr)-1):
        ans = val
        if arr[i][2]:
            ans -= arr[i][0]
            if nearstP != -1  and nearstP > i:
                ans += arr[nearstP][0]
                ans -= arr[nearstP][1]
                ans += arr[-1][1]
            else:
                ans += arr[-1][0]
        else:
            ans -= arr[i][1]
            if nearstT != -1  and nearstT > i:
                ans += arr[nearstT][1]
                ans -= arr[nearstT][0]
                ans += arr[-1][0]
            else:
                ans += arr[-1][1]
        res.append(ans)
    res.append(sum(pro) + sum(test))
    print(*res)
        
    


    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
