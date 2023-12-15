t = int(input())
for _ in range(t):
    n = int(input())
    num = []
    for _ in range(n):
        x,y = map(int,input().split())
        num.append([x,y])
    val = num[0][1]
    ans = num[0][0]
    flag = 1
    for i in range(1,len(num)):
        if num[i][1] >= val and num[i][0] >= ans:
            flag = 0
            break
    if flag:
        print(ans)
    else:
        print(-1)
            