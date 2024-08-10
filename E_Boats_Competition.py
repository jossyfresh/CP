t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    if n == 1:
        print(0)
        continue
    min_ = arr[0] + arr[1]
    max_ = arr[-1] + arr[-2]
    ans = 0
    for i in range(min_,max_+1):
        l = 0 
        r = n - 1
        count = 0
        while l < r:
            if arr[l] + arr[r] == i:
                l += 1
                r -= 1
                count += 1
            elif arr[l] + arr[r] < i:
                l += 1
            else:
                r -= 1
        ans = max(ans,count)
    print(ans)