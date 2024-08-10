t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i+1] = 'a'
            ans += 1
    print(ans)