n = int(input())
num = list(map(int,input().split()))
visited = set()
num.sort()
res = 1 
n = len(num)
for i in range (0,n):
    if num[i] <= res:
        res = res + num[i]
    else:
        break
print(res)


