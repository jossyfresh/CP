from bisect import bisect_left
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
for i in range(n):
    x = int(input())
    b = bisect_left(num,x)
    l = len(num) - b
    if l < len(num) and l > len(num)//2:
        print("YES")
    else:
        print("NO")
    