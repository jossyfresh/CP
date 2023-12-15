t = int(input())
for _ in range(t):
    n = int(input())
    ans = [2,4]
    cur = 4
    while len(ans) < n:
        cur += 3
        ans.append(cur)
    print(*ans)