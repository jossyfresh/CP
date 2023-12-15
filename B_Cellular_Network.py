n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
min_ = min(a)
max_ = max(a)
a.sort()
b.sort()
ans = []
l = 0
r = 0
while l < len(b) and r < len(a):
    if l < len(b)-1:
        if abs(b[l] - a[r]) < abs(b[l+1] - a[r]):

            ans.append(abs(b[l] - a[r]))
            r += 1
        else:
            l += 1
    else:

        ans.append(abs(b[l] - a[r]))
        r += 1
print(max(ans))

    