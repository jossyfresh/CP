n,x = map(int,input().split())
i = 1
ans = 0
for t in range(n):
    start,end = map(int,input().split())
    while i+x <= start:
        i += x
    ans += (end - i) + 1
    i = end + 1
print(ans)
    

    