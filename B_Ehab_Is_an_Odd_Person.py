n = int(input())
num = list(map(int,input().split()))
n = []
for x in num:
    if x % 2 == 0:
        n.append(1)
    else:
        n.append(0)
n = set(n)
if len(n) > 1:
    num.sort()
    print(*num)
else:
    print(*num)