t = int(input())
for _ in  range(t):
    n,k = map(int,input().split())
    l = k
    j = 0
    ans = 0
    while l :
        ans += (n ** j) * (l & 1)
        l >>= 1
        j+=1
    print(ans % (10**9 + 7))
