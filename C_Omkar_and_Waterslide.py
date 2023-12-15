t = int(input())
for a in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    max_ = 0
    m = {}
    res = 0
    for l in range(len(num)-1):
        res += max(num[l] - num[l+1],0)
    for i,x in enumerate(num):
        max_ = max(max_,x)
        m[i] = max_
    ans = [0]*len(num)
    for j in range(len(num)):
        if num[j] <= m[j]:
            ans[j] = m[j]-num[j]
    count = 0
    temp = 0
    for x in ans:
        if x == 0:
            count += temp
            temp = 0
        else:
            temp = max(temp,x)
    count += temp
    print(res)




