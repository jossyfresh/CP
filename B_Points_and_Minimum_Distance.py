t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    num.sort()
    arr = []
    l = 0 
    r = len(num)-1
    path = 0
    while l <= r:
        arr.append((num[l],num[r]))
        l += 1
        r -= 1
    prevx,prevy = arr[0]
    for i in range(1,n):
        nowx,nowy = arr[i]
        path = (abs(prevx-nowx) + abs(prevy-nowy))
        nowx = prevx
        nowy = prevy
    print(path)
    for x,y in arr:
        print(x,y)
