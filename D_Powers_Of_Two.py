num , size = map(int,input().split())

val = 1
count = 0
while val <= num:
    if num & val:
        count += 1
    val <<= 1
if size < count or num < size:
    print("NO")
else:
    ans = []
    val = 1
    p = 0
    while val <= num:
        if num & val:
            ans.append(2**p)
        p += 1
        val <<= 1
    ans.sort()
    idx = -1
    
    while len(ans) < size:
        if ans[idx]!= 1:
            
            ans[idx] //=2
            ans.append(ans[idx])
            idx = -1
        else:
            idx -=1 
    print("YES")
    print(*ans)