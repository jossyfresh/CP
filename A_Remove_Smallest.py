t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    num.sort()
    flag = 0
    for i in range(len(num)-1):
        if abs(num[i]-num[i+1]) > 1:
            flag = 1
    if flag:
        print("NO")
    else:
        print("YES")