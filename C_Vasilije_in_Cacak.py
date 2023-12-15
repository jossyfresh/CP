t = int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    max_ = (k*(n-k+1+n))//2
    min_ = k/2 * (k+1)
    if x >= min_ and x <= max_:
        print("YES")
    else:
        print("NO")



