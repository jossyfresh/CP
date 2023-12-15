from collections import defaultdict
n,k = map(int,input().split())
a = input()
b = list(a)
count = defaultdict(int)
l,r = 0,0
ans = 0
while r < len(a):
    while min(count["a"],count["b"]) > k:
        count[a[l]] -= 1
        l += 1
    count[a[r]] += 1
    ans = max(ans,r-l)
    r += 1
if min(count["a"],count["b"]) <= k:
    ans = max(ans,r-l)
print(ans)
