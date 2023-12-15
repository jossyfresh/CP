t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = 0
    y = min(nums)
    for x in nums:
        ans += x - y
    print(ans)