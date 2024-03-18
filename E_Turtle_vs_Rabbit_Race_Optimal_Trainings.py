def optimal_trainings(arr ,left , val , section):
    u = sum(arr[left : val + 1])
    ans = 0
    idx = 0
    if u > section:
        return True
    return False

test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    ans = []
    for __ in range(m):
        max_val = 0
        left , section = map(int, input().split())
        max_val = 
        left -= 1
        right = n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if optimal_trainings(arr ,left , mid , section):
                right = mid
            else:
                left = mid
        ans.append(right)
    print(*ans)