t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    min_ = float('inf')
    val = 0
    for i in range(len(a)):
        if a[i] < min_:
            val = i
            min_ = a[i]
    a[val] = min_+1
    total = 1
    for i in range(len(a)):
        total *= a[i]
    print(total)
