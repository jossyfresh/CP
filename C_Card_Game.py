n = int(input())
m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort(reverse=True)
m.sort(reverse=True)

p = 0
j = 0
a = 0
for i in range(n):
    if l[j] >= m[i]:
        p += 1
        j += 1
    else:
        l.pop()
        a += 1
if p > n//2:
    print("YES")
else:
    print("NO")
