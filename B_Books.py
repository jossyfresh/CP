n,t = map(int,input().split())
a = list(map(int,input().split()))
l = 0
r = 0
count = 0
time = 0
while r < n:
    while r < n and a[r] + time <= t:
        time += a[r]
        r += 1
    count = max(count,r-l)
    while r < n and a[r] + time > t:
        time -= a[l]
        l += 1
print(count)
