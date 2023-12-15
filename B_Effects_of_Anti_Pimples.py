n = int(input())
num = list(map(int,input().split()))
num.sort(reverse=True)
ans = 0
for i in range(n):
    ans += ((2**(n-i))-1) * num[i]
print(ans)
