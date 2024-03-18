import math
t = int(input())
for _ in range(t):
    a,b,l = map(int,input().split())
    count = 0
    arr = set()
    for i in range(20):
        for j in range(20):
            num = (a ** i) * (b ** j)
            if l % num == 0:
                arr.add(l//num)
    print(len(arr))
    
            