t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    def check(n,a,b):
        if n < min(a,b):
            return False
        return True
    l = -1
    r = (a+b)//4
    while r - l > 1:
        mid = (l+r)//2
        if check(mid,a,b):
            r = mid
        else:
            l = mid
    print(r)