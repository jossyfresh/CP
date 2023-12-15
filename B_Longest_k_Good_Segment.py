t,k = map(int,input().split())
n = list(map(int,input().split()))
l = 0
r = 0
x = {}
ans = [[0,0,0]]
while r < len(n):
    while len(x) > k:
        x[n[l]] -= 1
        if x[n[l]] == 0:
            x.pop(n[l])
        l+=1
    x[n[r]] = x.get(n[r],0) + 1
    if len(x) <= k:
        if r-l > ans[0][0]:
            ans[0] = [r-l,r,l]
    r += 1
res = [0,0,0]
while len(x) > k:
    x[n[l]] -= 1
    if x[n[l]] == 0:
        x.pop(n[l])
        l+=1
res = ans[0]
print(res[2]+1,res[1]+1)
