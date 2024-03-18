t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    flag = False
    for i in range(n):
        val = str(arr[i])
        if len(val) == 1:
            ans.append(val)
