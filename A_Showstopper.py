t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if b[-1] < max(b) and a[-1] >= max(b):
        a[-1],b[-1] = b[-1],a[-1]
    if a[-1] < max(a) and b[-1] >= max(a):
        a[-1],b[-1] = b[-1],a[-1]
    for i in range(n-1):
        if b[i] > b[-1] and a[i] <= b[-1]:
            b[i],a[i] = a[i],b[i]
        if b[-1] == max(b):
            break
    for i in range(n-1):
        if a[i] > a[-1] and b[i] <= a[-1]:
            a[i],b[i] = b[i],a[i]
        if a[-1] == max(a):
            break
    if a[-1] == max(a) and b[-1] == max(b):
        print("Yes")
    else:
        print("No")
    