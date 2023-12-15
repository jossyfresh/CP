t = int(input())
for a in range(t):
    n,h = map(int,input().split())
    num = list(map(int,input().split()))
    def check(k):
        res = 0
        i = 0
        while i < len(num)-1:
            res += min(k,num[i+1] - num[i])
            i+=1
        res+=k
        return res
    l = -1
    r = 10**18
    while r-l >1:
        mid = (l+r)//2
        if check(mid) >= h:
            r = mid
        else:
            l = mid
    print(r)