n,h = map(int,input().split())
num = list(map(int,input().split()))
ans = len(num)
for x in num:
    if x > h:
        ans += 1
print(ans)