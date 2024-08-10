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
    password = string()
    for i in range(len(password)):
        if not password[i].isalnum():
            print("NO")
            return
    for i in range(len(password)):
        if password[i].isalpha() and not password[i].islower():
            print("NO")
            return
    
    # Check if there is no digit that comes after a letter
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i+1].isdigit():
            print("NO")
            return 
    
    # Check if all digits are sorted in non-decreasing order
    digits = [char for char in password if char.isdigit()]
    if digits != sorted(digits):
        print("NO")
        return 
    
    # Check if all letters are sorted in non-decreasing order
    letters = [char for char in password if char.isalpha()]
    if letters != sorted(letters):
        print("NO")
        return 
    print("YES")
    return 

    
    return

if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
