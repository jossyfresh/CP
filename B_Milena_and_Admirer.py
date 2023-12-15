t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(1,len(arr)):
        if (arr[i] < arr[i-1]):
            count = 0
            j = i
            while j > 0 and arr[i] < arr[j-1]:
                count += 1
                j -= 1
            ans += count * max(arr[i] - 1,1)
    print(ans)