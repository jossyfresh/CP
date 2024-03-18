import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if math.sqrt(total) == int(math.sqrt(total)):
        print("YES")
    else:
        print("NO")