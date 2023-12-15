n,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
l = k-1
if k == 0:
    if num[0] > 1:
        print(1)
    else:
        print(-1)
elif k == 1:
    if len(num) > 1 and num[k] == num[k-1]:
        print(-1)
    else:
        print(num[0])
elif k == n:
    print(num[-1])
elif num[l] != num[k]:
    print(num[l])
else:
    print(-1)