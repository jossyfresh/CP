t = int(input())
for _ in range(t):
    m = int(input())
    num = []
    nums = []
    ans = []
    for _ in range(m):
        n = int(input())
        x = list(map(int,input().split()))
        nums.append(x)
        num.append(set(x))
    num.append(set())
    l = len(num)-2
    while l > 0:
        num[l].update(num[l+1])
        l-=1
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            flag = 1
            val = nums[i][j]
            if val not in num[i+1]:
                ans.append(val)
                break
    if len(ans) < m:
        print(-1)
    else:
        print(*ans)