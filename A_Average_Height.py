t=  int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odd = []
    even = []
    for i in range(len(a)):
        if a[i] %2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    if len(odd) > len(even):
        ans = []
        ans = odd + even
        print(*ans)
    else:
        ans = even + odd
        print(*ans)