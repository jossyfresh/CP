import bisect
n = int(input())
num = list(map(int,input().split()))
num.sort()
m = int(input())
for _ in range(m):
    x = int(input())
    ind = bisect.bisect_right(num,x)
    print(ind)