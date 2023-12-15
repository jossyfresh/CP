n = int(input())
num = list(map(int,input().split()))
ans = 0
for x in num:
    val = x/100
    ans += val

print((ans/n)*100)