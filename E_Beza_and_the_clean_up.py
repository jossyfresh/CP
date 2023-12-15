n,m,s,a,b = map(int,input().split())
numa = list(map(int,input().split()))
numb = list(map(int,input().split()))
numa.sort(reverse=True)
numb.sort(reverse=True)
l = 0
r = 0
ans = 0
while l < len(numa) and r < len(numb) and s > 0:
    if numa[l] > numb[r]:
        ans += numa[l]
        s -= a
        l += 1
    elif numa[l] < numb[r]:    
        ans += numb[r]
        s -= b
        r += 1
    else:
        if a < b:
            ans += numa[l]
            s -= a
            l += 1
        else:
            ans += numb[r]
            s -= b
            r += 1 
print(ans)

