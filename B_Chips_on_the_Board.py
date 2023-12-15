t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    min_a = min(a)
    min_b = min(b)
    suma = sum(a)
    sumb = sum(b)
    ans = min(min_a*n+sumb,min_b*n+suma)
    print(ans)
    
        