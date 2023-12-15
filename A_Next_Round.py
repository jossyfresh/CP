n,k = map(int,input().split())
num = list(map(int,input().split()))
ans = 0
for i in range(n):
    
    if num[i] >= num[k-1] and num[i] > 0:
        ans += 1
print(ans)