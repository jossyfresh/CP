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
    a = input()
    stack = []
    ans = 0
    for i,ch in enumerate(a):
        if stack:
            if ch == ")" and stack[-1][0] == "(":
                ans += i - stack[-1][1] 
                stack.pop()    
            elif ch == ")" and stack[-1][0] == "_":
                ans += i - stack[-1][1] 
                stack.pop()
            elif ch == "_" and stack[-1][0] == "(":
                ans += i - stack[-1][1] 
                stack.pop()
            elif ch == "_" and stack[-1][0] == "_":
                ans += i - stack[-1][1] 
                stack.pop()
            else:
                stack.append((ch,i))
        else:
            stack.append((ch,i))
    print(ans)
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
