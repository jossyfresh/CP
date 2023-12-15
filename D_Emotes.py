import math
n,m,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
a = nums[-1]
b = nums[-2]
ans = 0
if k == 1:
    x = math.ceil(m/2)
    ans += x * a
    ans += (m - x) * b
    print(ans)
else:
    x = math.floor(m/(k+1))
    if x != 0:
        ans += x * b
        ans += (m - x) * a
        print(ans)
    else:
        ans += k * a
        print(ans) 

