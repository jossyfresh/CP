n,a,b = map(int,input().split())
arr = list(map(int,input().split()))
l = arr[0]
total = sum(arr)
arr = arr[1:]
arr.sort()
ans = len(arr)
for i in range(len(arr)-1,-1,-1):
    val = (a * l) / total
    if val >= b:
        ans = len(arr) - i - 1
        break
    total -= arr[i]
print(ans)

