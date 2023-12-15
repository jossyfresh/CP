from collections import defaultdict


t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    new = defaultdict(int)
    for x in a:
        if x >= k:
            new[x%k] += 1
        else:
            new[k-x] += 1
    print(new)
    x = 0
    ans = 0
    for val in a:
        if val == 0:
            continue
        else:
            if val in new:
                new[val] -= 1
                if new[val] == 0:
                    new.pop(val)
                ans += 1
    print(ans)
            



