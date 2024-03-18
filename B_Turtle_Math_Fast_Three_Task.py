t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    ans = 0
    flag = False
    if total % 3 == 0:
        flag = True
        ans = 0
    else:
        for i in range(len(arr)):
            if (total - arr[i]) % 3 == 0:
                ans = 1
                flag = True
                break
    if not flag:
        ans = 3 - (total % 3)
    print(ans)

    
    