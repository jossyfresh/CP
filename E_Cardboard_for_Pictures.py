t = int(input())
for _ in range(t):
    n,c = map(int,input().split())
    arr = list(map(int,input().split()))
    def check(mid,arr):
        area = 0
        for i in range(len(arr)):
            area += (arr[i] + (2*mid)) * (arr[i] + (2*mid))
        return area
    l = 0
    r = 10**18
    while (l < r):
        mid = (l + r )//2
        if check(mid,arr) < c:
            l = mid + 1
        elif check(mid,arr) > c:
            r = mid
        else:
            print(mid)
            break
    
        