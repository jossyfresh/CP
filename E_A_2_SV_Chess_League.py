n,k = map(int,input().split())
num = list(map(int,input().split()))
def mergesort(a,b,arr):
    if a == b:
        return [(arr[a],a)]
    mid = a + (b- a) // 2
    left = mergesort(a,mid,arr)
    right = mergesort(mid+1,b,arr)
    return merge(left,right)
def merge(le,ri):
    r = 0
    l = 0
    new = []
    maxl = min(le)
    maxr = min(ri)
    ml = maxl[0]
    mr = maxr[0]
    while l < len(le) and r < len(ri):
        if le[l][0] > ri[r][0]:
            if mr - le[l][0] <= k:
                new.append(le[l])
            l+=1
        else:
            if ml - ri[r][0] <= k:
                new.append(ri[r])
            r+=1
    while l < len(le):
        if mr - le[l][0] <= k:
            new.append(le[l])
        l+=1
    while r < len(ri):
        if ml - ri[r][0] <= k:
            new.append(ri[r])
        r+=1
    return new
val = mergesort(0,len(num)-1,num)
val.sort(key = lambda x:x[1])
ans = []
for x in val:
    ans.append(x[1]+1)
print(*ans)



