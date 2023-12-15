n = int(input())
ans = 0
for _ in range(n):
    x,y = map(int,input().split())
    if y - x >= 2:
        ans += 1
print(ans)