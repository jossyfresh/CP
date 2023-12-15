import bisect
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    ans = [0]*n
    for i in range(n):
        ind = bisect.bisect_left(arr[i])