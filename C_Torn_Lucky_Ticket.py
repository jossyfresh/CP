from collections import defaultdict
n = int(input())
arr = list(map(str,input().split()))
map = defaultdict(int)
ans = 0
for s in arr:
    total = 0
    for i in range(len(s)):
        total += int(s[i])
    res = 0
    value = [len(s[i]),()]
    for i in range(len(s)):
        res += int(s[i])
        value[1] = (total-res,i)
        map[tuple(value)] += 1


         