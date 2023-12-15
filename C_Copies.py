n,x,y = map(int,input().split())
l = -1
r = 2*(10**9) + 1000 
def check(mid):
    one = (mid//x)
    two = mid//y
    if (one + two) >=  n-1:
        return True
    return False
if n == 1:
    print(min(x,y))
else:
    while l < r:
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r+ min(x,y))