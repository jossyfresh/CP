n,k = map(int,input().split())
num = list(map(int,input().split()))
visited = set()
memo = {}
def dp(i,Sum):
    if i == len(num) or Sum >= k:
        if Sum <= k:
            visited.add(Sum)
        return 
    if (i,Sum) in memo:
        return 
    a = dp(i+1,Sum + num[i])
    b = dp(i+1,Sum)
    memo[(i,Sum)] = 1
    return 
dp(0,0)
print(len(visited))
print(*visited)
