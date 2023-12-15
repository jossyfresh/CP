import math
t = int(input())
for _ in range(t):
    px,py = map(int,input().split())
    ax,ay = map(int,input().split())
    bx,by = map(int,input().split())
    def check(radius):
        disab = math.sqrt((ax-bx)**2 + (ay-by)**2)
        disap = math.sqrt((ax-px)**2 + (ay-py)**2)
        disbp = math.sqrt((bx-px)**2 + (by-py)**2)
        disao = math.sqrt(ax**2 + ay**2)
        disbo = math.sqrt(bx**2 + by**2)
        if (disap <= radius and disao <= radius ) or (disbp <= radius and disbo <= radius):
            return True
        if (disao <= radius or disbo <= radius) and (disap <= radius or disbp <= radius):
            if disab <= 2*radius:
                return True
        return False
    l = 0
    r = 10**6
    while l + 0.0000000001 < r:
        mid = (l+r)/2
        if check(mid):
            r = mid
        else:
            l = mid 
    print(l)