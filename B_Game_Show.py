k,n = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0
for i in range(2,(10**4)+1):
    val = i
    count = 0
    money = k
    for j in range(len(nums)):
        if nums[j] % val == 0 and val > 1:
            count += 1
            continue
        if money < nums[j]:
            break
        count += 1
        money -= nums[j]
    ans = max(ans,count)
print(ans)


