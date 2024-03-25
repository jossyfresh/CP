n,m = map(int, input().split())
arr = []
sum = 0
for i in range(n):
    x,y = map(int, input().split())
    arr.append((x-y))
    sum += x
arr.sort(reverse=True)
for i in range(len(arr)):
    if sum <= m:
        print(i)
        exit()
    sum -= arr[i]
if sum <= m:
    print(n)
else:
    print(-1)
