n,k,d = map(int,input().split())
memo = {}
c = False
def dfs(n,c):
    if (n,c) in memo:
        return memo[(n,c)]
    if n == 0:
        if c:
            return 1
        else:
            return 0
    if n < 0:
        return 0
    val = 0
    for i in range(1,k+1):
        if i >= d:
            val += dfs(n-i,True)
        else:
            val += dfs(n-i,c)
    
    memo[(n,c)] = val
    return memo[(n,c)]
print((dfs(n,c))%((10**9)+7))