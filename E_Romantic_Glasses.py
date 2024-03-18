import math,random
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    val = random.randint(0,10**4)
    pre = {0 ^ val}
    total = 0
    ans = 0
    for i in range(len(arr)):
        x = arr[i]
        if i % 2 == 0:
            x *= -1  
        total += x
        ntotal = total ^ val
        if ntotal in pre:
            ans = 1
            break
        pre.add(ntotal)
    if ans > 0:
        print("YES")
    else:
        print("NO")
