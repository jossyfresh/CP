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
    n,m = map(int, input().split())
    a = li()
    b = li()
    names = ["Lidiya Abebe","melat tesfaye","Eyoab amare","Adey Ebuy","Surafel Fikre","Natnael Birhanu","Olman Gemechu","Hermela Ashagre","Hibreselam Dejene","Lemesa Elias","Abebe Megibar","Izzat engida","kaletsidike ayalew","hiwot addis","Liben Adugna","Chapa Eresso","Betelhem Negash","Hermela Mulugeta","Gadisa Yusuf"]
    for i in range(len(names)):
        names[i] = names[i].lower()
    names.sort()
    for name in names:
        print(name)
if __name__ == "__main__":
    fast_io()
    t = int(input())
    for _ in range(t):
        solve()
