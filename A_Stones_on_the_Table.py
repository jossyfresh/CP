n = int(input())
a = input()
l = 0
r = 1
ans = 0
while r < len(a):
    if a[l] == a[r]:
        ans += 1
        r += 1
    else:
        l = r
        r += 1
print(ans)
