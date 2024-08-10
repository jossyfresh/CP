import math
t = int(input())
for _ in range(t):
    n = int(input())
    max_ = 0
    ans = 0
    for i in range(n-1,-1,-1):
        val = math.gcd(n,i) + i
        if val > max_:
            max_ = val
            ans = i
    print(ans)