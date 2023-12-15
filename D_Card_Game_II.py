n = int(input())
m = list(map(int,input().split()))
l = list(map(int,input().split()))
m.sort(reverse=True)
l.sort(reverse=True)

x = 0
val = 0
j = 0
for i in range(n):
    if l[j] >= m[i]:
        j += 1
    else:
        if val:
            val -= 1
        else:
            val += 1
            x += 1
print(x)
