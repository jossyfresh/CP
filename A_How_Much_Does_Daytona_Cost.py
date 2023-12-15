from collections import Counter
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    num = list(map(int,input().split()))
    count = Counter(num)
    flag = 0
    if k in num:
        flag = 1
    if flag:
        print("YES")
    else:
        print("NO")
