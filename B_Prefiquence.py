t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = input()
    b = input()
    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if a[i] == b[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    print(count)