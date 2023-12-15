n=int(input())
a=[0]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
s=sum(x[1] for x in a)
x=10000
dp=[-10**9]*x
dp[0]=0
print(a)
for v,w in a:
    for i in range(x-1,v-1,-1):
        print(i)
        dp[i]=max(dp[i],dp[i-v]+w)
for i in range(x):
    if i>=s-dp[i]:
        print(i)
        break