t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr= list(map(int,input().split()))
    p = 1
    for i in range(len(arr)):
        p *= arr[i]
    if 2023 % p == 0:
        nw = []
        f = 2023 // p
        nw.append(f)
        for i in range(k-1):
            nw.append(1)
        print('YES')
        print(*nw)
    else:
        print("NO")
