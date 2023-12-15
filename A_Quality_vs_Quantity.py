import math
t= int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    num.sort()
    new = []
    Sum = 0
    for i in range(len(num)):
        Sum += num[i]
        new.append(Sum)
    minsize = math.ceil(len(num)/2) - 1
    l = 0
    r = len(num)-1
    Sum = 0
    flag = 0
    while l < minsize:
        Sum += num[r]
        r-=1
        l+=1
    max_ = Sum
    i = minsize
    while i <= r:
        if new[i] < max_:
            flag = 1
        i+=1
    if flag:
        print("YES")
    else:
        print("NO")    
