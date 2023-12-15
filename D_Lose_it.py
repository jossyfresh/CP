from collections import Counter
n = int(input())
nums = list(map(int,input().split()))
check = [4,8,15,16,23,42]
ans = 0
count = Counter(nums)
if len(nums) < 6:
    ans = len(nums)
elif len(nums) == 6:
    if nums == check:
        ans = 0 
    else:
        ans = 6
else:
    if len(nums) % 6 != 0:
        c = len(nums) // 6
        min_ = float('inf')
        for x in check:
            min_ = min(min_,count[x])
        ans = len(nums) - (min_) * 6
        
    else:
        min_ = float('inf')
        for x in check:
            min_ = min(min_,count[x])
        ans = len(nums) - (min_) * 6
print(ans)
