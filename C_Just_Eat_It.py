t= int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    first = a[:n-1]
    second = a[1:n]
    res = 0
    dp = [0]*len(first)
    dp[0] = first[0]
    ans = dp[0]
    for i in range(1,len(first)):
        dp[i] = max(first[i],first[i]+dp[i-1])
        ans = max(ans,dp[i])
    res = max(ans,res)
    dp2 = [0]*len(second)
    dp2[0] = second[0]
    ans1 = dp2[0]
    for i in range(1,len(second)):
        dp2[i] = max(second[i],second[i]+dp2[i-1])
        ans1 = max(ans,dp2[i])
    res = max(ans1,res)
    if sum(a) > res:
        print("YES")
    else:
        print("NO")
    