n = int(input())
a = list(map(int,input().split()))
b =  list(map(int,input().split()))
l = 0
visited = set()
for i in range(len(b)):
    if b[i] != a[l] and a[l] not in visited:
        visited.add(b[i])
        visited.add(a[l])
    else:
        l += 1
print(len(visited))
