t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    for i in range(n):
        x = 0
        for j in range(n):
            if j == i:
                continue
            x = x ^ num[j]
        if x == num[i]:
            print(num[i])
            break
