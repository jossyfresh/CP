t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]
    print(sum(arr))