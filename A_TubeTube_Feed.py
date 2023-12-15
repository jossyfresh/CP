q = int(input())
for _ in range(q):
    n,t  = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    nums = []
    for i in range(n):
        nums.append([a[i],b[i],i])
    for i in range(n):
        nums
