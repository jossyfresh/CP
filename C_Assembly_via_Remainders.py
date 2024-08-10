t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [max(arr)]
    for i in range(len(arr)):
        if ans[-1] < arr[i]:
            val = arr[i]
        else:   
            val = ans[-1] + arr[i]
        ans.append(val)
    print(*ans)