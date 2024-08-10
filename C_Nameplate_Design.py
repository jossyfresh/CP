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
    s = string()
    len_ = 1
    while math.ceil(len(s) / len_ > 20):
        len_ += 1
    row = len_
    col = math.ceil(len(s) / len_)
    stars = row * col - len(s)
    print(row,col)
    start = 0
    for i in range(row):
        if stars > 0:
            print(s[start:start+col-1] + "*")
            stars -= 1
            start += col - 1
        else:
            print(s[start:col+start])
            start += col

    


    return

if __name__ == "__main__":
    fast_io()
    solve()
