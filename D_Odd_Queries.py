t = int(input())
for b in range(t):
    n,q = map(int,input().split())
    num = list(map(int,input().split()))
    pre = [0]
    val = 0
    for x in num:
        val += x
        pre.append(val)
    for a in range(q):
        l,r,k = map(int,input().split())
        new = pre[r] - pre[l-1]
        ans = pre[-1] + k*(r-l+1) - new
        if ans % 2 == 0:
            print("NO")
        else:
            print("YES")