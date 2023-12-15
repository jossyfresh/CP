t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    flag = 0
    for i in range(n):
        if num[i] <= i+1:
            flag = 1
            break
    if flag:
        print("YES")
    else:
        print("NO")
