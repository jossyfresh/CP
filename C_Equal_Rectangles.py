q = int(input())
for t in range(q):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    i = 0
    flag = 0
    while i < len(nums):
        if nums[i] == nums[i+1]:
            i+=2
        else:
            flag = 1
            break
    i = 0
    r = len(nums)-1
    area = 0
    if not flag:
        while i < r:
            if area == 0:
                area = nums[i]*nums[r]
                i += 2
                r -= 2
            else:
                narea = nums[i]*nums[r]
                if narea == area:
                    i += 2
                    r -= 2
                else:
                    flag = 1
                    break
    if flag:
        print("NO")
    else:
        print("YES")
