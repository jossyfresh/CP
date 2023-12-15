import itertools
n = int(input())
num = list(map(int,input().split()))
comb = list(itertools.combinations(num,2))
ans = 0
