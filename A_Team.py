from collections import Counter
n = int(input())
ans = 0
for _ in range(n):
    x = Counter(list(map(int,input().split())))
    if x[1] >= 2:
        ans += 1
print(ans)