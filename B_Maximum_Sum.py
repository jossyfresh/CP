from collections import deque
t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    num = list(map(int,input().split()))
    num.sort()
    prefix = []
    Sum = 0
    for x in num:
        Sum += x
        prefix.append(Sum)
    ans = 0
    for i in range(k+1):
        total  = prefix[-1]
        if i == 0:
            ans = max(prefix[n - (k - i)]- num[n-(k-i)],ans)
        elif i == k:
            ans = max(ans,total - prefix[(2*i)-1])
        else:
            ans = max(((prefix[n - (k - i)]- num[n-(k-i)]) - prefix[(2*i)-1]),ans)
    print(ans)


        


