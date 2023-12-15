t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    val = int((x * (x + 1)) / 2)
    minus = 0
    arr.sort()
    for i in range(len(arr)): 
        if x >= arr[i]:
            minus += int(arr[i])
        else:
            break
    ans = val - 2*int(minus)
    print(int(ans))