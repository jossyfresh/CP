from collections import Counter
num = list(map(int,input().split()))
count = Counter(num)
ans = 0
for x in count:
    ans += count[x] - 1
print(ans)
