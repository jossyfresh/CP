n,k = map(int, input().split())
arr = list(map(int, input().split()))
candies = 0
for i in range(n):
    candies += arr[i]
    k -= min(8,candies)
    candies -= min(8,candies)
    if k <= 0:
        break
if k <= 0:
    print(i+1)
else:
    print(-1)
