n = int(input())
arr = list(map(int, input().split()))
mp = {}
for i in range(len(arr)):
    mp[arr[i]] = i+1
ans = []
for i in range(1, n+1):
    ans.append(mp[i])
print(*ans)


