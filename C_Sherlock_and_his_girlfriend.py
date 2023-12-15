n = int(input())
ans = [1] * n
for val in range(2,n+2):
    flag = 0
    d = 2
    while d * d <= val:
        if val % d == 0:
            flag = 1
        d += 1
    if flag:
        ans[val-2] = 2
    else:
        ans[val-2] = 1
print(len(set(ans)))
print(*ans)